from flask import request
from flask_restx import Resource, Namespace
from concurrent.futures import ThreadPoolExecutor
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from database import database
import recognize
import uuid

api_upload = Namespace('Upload', description='Uploads audio data to be processed')

upload_parser = api_upload.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)

@api_upload.route('/upload')
class UploadController(Resource):
    @api_upload.response(201, "Created")
    @api_upload.response(400, "Bad Request")
    @api_upload.expect(upload_parser)
    def post(self):
        print(request.files)
        f = request.files['file']
        if f.filename.endswith(".wav") or f.filename.endswith(".mp3"):
            file_id = str(uuid.uuid1())
            f.save("uploads/media/" + f.filename)
            db = database.Database()
            db.insert("audios", [file_id, f.filename])
            with ThreadPoolExecutor() as executor:
                future = executor.submit(RecognizeController.get(self, file_id))

            return {"id": file_id, "file": f.filename}, 201
        else:
            return {"error": "Not supported. Please, upload only WAV or MP3 files."}, 400

api_search = Namespace('Search', description='Search for uploaded scripts in database')

search_model = api_search.parser()
search_model.add_argument('id', location='id', type=str, required=True)

@api_search.route('/')
class SearchController(Resource):        
    @api_search.response(200, "OK")
    @api_search.response(404, "Not Found")
    def get(self):
        with open("media/files.csv", "r") as file:
            list_files = file.readlines()[1:]
            final_list = []
            for x in list_files:
                data = {
                    "id": x.split(",")[0].replace("\n", ""),
                    "file": x.split(",")[1].replace("\n", "")
                }
                final_list.append(data)
        return final_list, 200

@api_search.route('/<id>')
class Search(Resource):        
    @api_search.response(200, "OK")
    @api_search.response(404, "Not Found")
    def get(self):
        with open("media/files.csv", "r") as file:
            list_files = file.readlines()[1:]
            final_list = []
            for x in list_files:
                data = {
                    "id": x.split(",")[0].replace("\n", ""),
                    "file": x.split(",")[1].replace("\n", "")
                }
                final_list.append(data)
        return final_list, 200

api_recognize = Namespace('Recognize', description='Recognize human emotion and transcript audio speech')
@api_recognize.route('/<id>')
class RecognizeController(Resource):        
    @api_recognize.response(200, "OK")
    @api_recognize.response(404, "Not Found")
    def get(self, id):
        with open("media/files.csv", "r") as file:
            list_files = file.readlines()[1:]
            list_files = [x.split(",")[1].replace("\n", "") for x in list_files if x.split(",")[0].replace("\n", "") == id][0]
            predict = recognize.predictSound("media/" + list_files)
            message = recognize.returnText("media/" + list_files)
        return {"id": id, "file": list_files, "emotion": predict, "message": message}, 200

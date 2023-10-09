from flask import request
from flask_restx import Resource, Namespace
from werkzeug.datastructures import FileStorage
from database import database

import os
import json
import threading
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
            os.remove("uploads/media/" + f.filename)
            recognize = RecognizeController()
            thread = threading.Thread(target=recognize.get, args=(file_id,))
            thread.start()

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
        db = database.Database()
        final_list = db.select("audios")
        return final_list, 200

@api_search.route('/<id>',)
class Search(Resource):        
    @api_search.response(200, "OK")
    @api_search.response(404, "Not Found")
    def get(self, id):
        db = database.Database()
        final_list = db.select("recognition", id)[0]
        file_id, emotion, message, percentage = final_list
        final_list = {
            "id": file_id,
            "emotion": emotion,
            "transcript": message.decode("utf-8"),
            "percentage": percentage
        }
        return final_list, 200

api_recognize = Namespace('Recognize', description='Recognize human emotion and transcript audio speech')
@api_recognize.route('/<id>')
class RecognizeController(Resource):        
    @api_recognize.response(200, "OK")
    @api_recognize.response(404, "Not Found")
    def get(self, id):
        db = database.Database()
        audio_file = db.select("audios", id)[0][0]
        with open(f'uploads/media/{id}.wav', 'wb') as audio:
            audio.write(audio_file)
        predict = recognize.predictSound(f'uploads/media/{id}.wav')
        message, predict = recognize.returnText(f'uploads/media/{id}.wav')

        db.insert("recognition", [id, predict, message, f"{predict}%"])
        os.remove(f'uploads/media/{id}.wav')
        return {"id": id, "file": f'uploads/media/{id}.wav', "emotion": predict, "message": message}, 200

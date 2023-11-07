from flask import request
from flask_restx import Resource, Namespace
from werkzeug.datastructures import FileStorage
from database import database

import os
import threading
import recognize as rec
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
        try:
            print(request.files)
            f = request.files['file']
            if f.filename.endswith(".wav") or f.filename.endswith(".mp3"):
                print("Length:", request.content_length)
                if (request.content_length < 90000 and f.filename.endswith(".mp3")) or (request.content_length < 1000000 and f.filename.endswith(".wav")):
                    file_id = str(uuid.uuid1())
                    f.save("/usr/backend/uploads/" + f.filename)
                    rec.convertAudio("/usr/backend/uploads/" + f.filename)
                    filename = f.filename.replace(".mp3", ".wav")
                    db = database.Database()
                    
                    file_exists = db.check_file(filename)
                    if file_exists == False: 
                        db.insert("audios", [file_id, filename])
                        recognize = RecognizeController()
                        thread = threading.Thread(target=recognize.get, args=(file_id,))
                        thread.start()
                        thread.join()
                    else: 
                        file_id = file_exists[1]

                    os.remove("/usr/backend/uploads/" + filename)

                    return {"id": file_id, "file": filename}, 201
                else:
                    if f.filename.endswith(".mp3"): 
                        return {"error": f"Not supported. Please, upload only MP3 audios with maximum 90KB."}, 400
                    else: 
                        return {"error": f"Not supported. Please, upload only WAV audios with maximum 1MB."}, 400
            else:
                return {"error": "Not supported. Please, upload only WAV or MP3 files."}, 400
        except:
            return {"error": "Internal server error."}, 500

api_search = Namespace('Search', description='Search for uploaded scripts in database')
search_model = api_search.parser()
search_model.add_argument('id', location='id', type=str, required=True)

@api_search.route('/')
class SearchController(Resource):        
    @api_search.response(200, "OK")
    @api_search.response(404, "Not Found")
    def get(self):
        try:
            db = database.Database()
            final_list = db.select("audios")
            return final_list, 200
        except: 
            return {"error": "Internal server error."}, 500

@api_search.route('/<id>',)
class Search(Resource):        
    @api_search.response(200, "OK")
    @api_search.response(404, "Not Found")
    def get(self, id):
        try:
            db = database.Database()
            final_list = db.select("recognition", id)
            if len(final_list) > 0:
                file_id, emotion, message, percentage = final_list[0]
                final_list = {
                    "id": file_id,
                    "emotion": emotion,
                    "message": message,
                    "percentage": percentage
                }
                return final_list, 200
            else:
                return {"error": f"ID {id} not found"}, 404
        except: 
            return {"error": "Internal server error."}, 500

api_recognize = Namespace('Recognize', description='Recognize human emotion and transcript audio speech')

@api_recognize.route('/<id>')
class RecognizeController(Resource):        
    @api_recognize.response(200, "OK")
    @api_recognize.response(404, "Not Found")
    def get(self, id):
        try:
            db = database.Database()
            audio_file = db.select("audios", id)
            if len(audio_file) > 0:
                with open(f'/usr/backend/uploads/{id}.wav', 'wb') as audio:
                    audio.write(audio_file[0][0])
                emotion, predict = rec.predictSound(f'/usr/backend/uploads/{id}.wav')
                message = rec.returnText(f'/usr/backend/uploads/{id}.wav')

                try:
                    db.insert("recognition", [id, emotion, message, predict])
                    os.remove(f'/usr/backend/uploads/{id}.wav')
                except: 
                    db.update("recognition", [id, emotion, message, predict])

                return {"id": id, "file": f'/usr/backend/uploads/{id}.wav', "emotion": emotion, "predict": predict, "message": message}, 200
            else:
                return {"error": f"Audio with ID {id} not found"}, 404
        except: 
            return {"error": "Internal server error."}, 500
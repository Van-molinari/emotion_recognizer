from flask import request
from flask_restx import Resource, Namespace, fields
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import uuid

api = Namespace('Recognize', description='Recognize human emotion and transcript audio speech')

upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)

search_model = api.model('SearchModel', {
    'id': fields.String(description='Audio ID', type='str', required=True)
})

@api.route('/')
class UploadController(Resource): 
    @api.response(201, "Created")
    @api.response(400, "Bad Request")
    @api.expect(upload_parser)
    def post(self):
        print(request.files)
        f = request.files['file']
        if f.filename.endswith(".wav") or f.filename.endswith(".mp3"):
            file_id = str(uuid.uuid1())
            with open("media/files.csv", "+a") as file:
                line = "\n" + file_id + "," + f.filename
                file.write(line)
            f.save("media/" + secure_filename(f.filename))
            return {"id": file_id, "file": f.filename}, 201
        else:
            return {"error": "Not supported. Please, upload only WAV or MP3 files."}, 400
        
@api.route('/search')
class SearchController(Resource):        
    @api.response(200, "OK")
    @api.response(404, "Not Found")
    @api.expect(search_model)
    def get(self):
        return "Get ok", 200

# @api.route('/r')
# class Recognize(Resource):
#     @api.route('/upload', methods=['POST'])
#     def upload_figele(self, ):
#         return render_template('/Users/vanessamolinari/Documents/Ciência da Computação/TCC/Protótipo/app/templates/upload.html')

#     @api.route('/uploadAudio', methods = ['GET', 'POST'])
#     def upload(self, ):
#         if request.method == 'POST':
#             f = request.files['file']
#             f.save(secure_filename(f.filename))
#             return 'file uploaded successfully'

#     @api.route('/recognize')
#     def recognize(self, ):
#         print('Post recebido')
#         # text = request.json['text']
#         file = request.files['audio']
#         # Salva o arquivo como um arquivo temporário no formato PCM WAV
#         with tempfile.NamedTemporaryFile(suffix='.wav') as f:
#             file.save(f.name)
#             audio_info = pydub.utils.mediainfo(f.name)
#             # Converta o arquivo para PCM Wave usando o ffmpeg
#             cmd = ['ffmpeg', '-i', f.name, '-acodec', 'pcm_s16le', '-ar', '16000', f.name + '.wav']
#             subprocess.check_output(cmd)
#             audio = sr.AudioFile(f.name + '.wav')
#             with audio as source:
#                 audio_data = sr.Recognizer().record(source)

#         recognized_text = sr.Recognizer().recognize_google(audio_data, language="pt-BR")
#         response = f'Você disse: {recognized_text}'
#         print(response)

#         return response, 200, {'Content-Type': 'application/json; charset=utf-8'}
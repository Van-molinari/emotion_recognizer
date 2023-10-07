from flask import Flask, Blueprint, render_template
from flask_restx import Api
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

from app.controllers import routes

app = Flask(__name__)
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)

api = Api(app,
          version='1.0',
          title='Recognize',
          description='Audio Recognition API Project',
          doc='/docs')

api.add_namespace(routes.api_upload, path='/data')
api.add_namespace(routes.api_search, path='/search')
api.add_namespace(routes.api_recognize, path='/recognize')
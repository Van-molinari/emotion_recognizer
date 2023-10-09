from app import app
from os import environ

if __name__ == '__main__':
    SERVER_HOST = environ.get('SERVER_HOST', 'localhost')
    app.run(host='0.0.0.0',port=5500, debug=(not environ.get('ENV') == 'PRODUCTION'),threaded=True)

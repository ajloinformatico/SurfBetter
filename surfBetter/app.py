from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS # it must be comment into deployment
from api.HelloApiHandler import HelloApiHandler # get and post requests

# instance of Flask indicating with staic_url_path I spacefy a diferent path for the static file
# with static folder indicate where is my client or "templates"
app = Flask(__name__, static_url_path='', static_folder='frontend/build')

# its use to disable error when we make an Api request to a diferent domain
CORS(app) # it must be comment into deployment
api = Api(app)

# Routes default 
# load "view"
@app.route("/", defaults={'path':''})
def serve(path):
    """ 
    with send_from_directory() allow flask to send index.html dorm static_file
    declare in app
    Returns:
        [type]: [description]
    """
    return send_from_directory(app.static_folder,'index.html')

# load rest
api.add_resource(HelloApiHandler, '/flask/hello')
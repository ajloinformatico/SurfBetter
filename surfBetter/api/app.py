from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS  # it must be comment into deployment
# first option
from controllers import ExampleModel, UserController  # get and post requests

# second option
from routes.user_controller import user_routes

from models import db

# from database.MysqlLite import *

# instance of Flask indicating with staic_url_path I spacefy a diferent path for the static file
# with static folder indicate where is my client or "templates"
app = Flask(__name__, static_url_path='', static_folder='../frontend/build')

# its use to disable error when we make an Api request to a diferent domain
CORS(app)  # it must be comment into deployment
api = Api(app)

db.create_all()


# Routes default
# load "view"
@app.route("/", defaults={'path': ''})
def serve(path):
    """ 
    with send_from_directory() allow flask to send index.html dorm static_file
    declare in app
    Returns:
        [static folder]: [surfbetter index]
    """
    return send_from_directory(app.static_folder, 'index.html')


app.register_blueprint(user_routes)
app.run()

"""
# URLS FOR API END POINTS -> (MODEL.VIEW,'URL')
api.add_resource(ExampleModel.ExampleRoute, "/")
api.add_resource(UserController, "/login")
api.add_resource(UserController, "/singin")
api.add_resource(UserController, "/logout")
"""




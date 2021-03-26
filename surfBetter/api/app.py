from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS  # it must be comment into deployment
from HelloApiHandler import HelloApiHandler  # get and post requests
from flask_sqlalchemy import SQLAlchemy

# from database.MysqlLite import *

# instance of Flask indicating with staic_url_path I spacefy a diferent path for the static file
# with static folder indicate where is my client or "templates"
app = Flask(__name__, static_url_path='', static_folder='../frontend/build')

# config Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/surfbetter.db'

# DataBase
db = SQLAlchemy(app)

# its use to disable error when we make an Api request to a diferent domain
CORS(app)  # it must be comment into deployment
api = Api(app)


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


# load rest Api
api.add_resource(HelloApiHandler, '/flask/hello')

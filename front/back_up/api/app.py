from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy  # database
from flask_cors import CORS  # it must be comment into deployment

# instance SQLALchemy for te models
db = SQLAlchemy()

# app with front
app = Flask(__name__, static_url_path='', static_folder='../frontend/build')

app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/surfbetter.db'

# init SQLAlchemy
db.init_app(app)

# its use to disable error when we make an Api request to a diferent domain
CORS(app)  # it must be comment into deployment


@app.route("/", defaults={'path': ''})
def serve(path):
    """
    with send_from_directory() allow flask to send index.html dorm static_file
    declare in app
    Returns:
        [static folder]: [surfbetter index]
    """
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run()



# TODO: Redoo all pages

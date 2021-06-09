from flask import Flask
import flask_cors
import os
from extensions import db, guard
from models import User
from routes_user import routes_user
from routes_beaches import routes_beaches
from routes_comments_likes import routes_comments_likes
from image_service import api_images
from gmail_service import gmail_service
from seed_user import seed_user
from seed_beach import seed_beaches, seed_description_points
from seed_comments_likes import seed_likes, seed_comments, seed_likes_of_comment


def create_app():
    """
    return instance of the api
    """

    # initialize cors to allow requests (develop)
    cors = flask_cors.CORS()

    # intialize flask basic conf & basic conf
    app = Flask(__name__)
    app.debug = False
    app.config['SECRET_KEY'] = 'top secret'
    app.config['JWT_ACCESS_LIFESPAN'] = {'hours': 24}
    app.config['JWT_REFRESH_LIFESPAN'] = {'days': 30}

    # initialize sqlite database TODO IF FAILS CHANGE TO SIMETHINF LIKE THAT : app.config['SQLALCHEMY_DATABASE_URI']
    #  = F"sqlite:///{os.path.join(os.getcwd(), 'database.db')}"
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database/database.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.getcwd()}/database/database.db"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # initialize cors to debug
    cors.init_app(app)

    # flask pretorian initialize (app, model)
    guard.init_app(app, User)

    # Seeders
    seed_user(app)
    seed_description_points(app),
    seed_beaches(app)
    seed_likes(app)
    seed_comments(app)
    seed_likes_of_comment(app)

    # Load api routes blueprint module
    app.register_blueprint(routes_user)
    app.register_blueprint(routes_comments_likes)
    app.register_blueprint(routes_beaches)

    # Load gmail service
    app.register_blueprint(gmail_service)

    # Load api images routes blueprint module
    app.register_blueprint(api_images)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)

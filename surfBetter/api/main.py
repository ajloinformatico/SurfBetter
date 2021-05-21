from flask import Flask
import flask_cors 
from extensions import db, guard
from models import User
from routes import routes
from image_service import api_images
from seeders.seed_user import seedUser

# TODO MAYBE I WILL DELETE IT


def create_app():
    """
    return instance of the api
    """

    # initialize cors to allow requests (develop)
    cors = flask_cors.CORS()  
    
    # intialize flask basic conf & basic conf
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = 'top secret'
    app.config['JWT_ACCESS_LIFESPAN'] = {'hours': 24}
    app.config['JWT_REFRESH_LIFESPAN'] = {'days': 30}

    # initialize sqlite database TODO IF FAILS CHANGE TO SIMETHINF LIKE THAT : app.config['SQLALCHEMY_DATABASE_URI'] = F"sqlite:///{os.path.join(os.getcwd(), 'database.db')}"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database/database.db"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # initialize cors to debug
    cors.init_app(app)

    # flask pretorian initialize (app, model)
    guard.init_app(app, User)

    # Seeders
    seedUser(app)

    # Load api routes blueprint module
    app.register_blueprint(routes)

    # Load api images routes blueprint module
    app.register_blueprint(api_images)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
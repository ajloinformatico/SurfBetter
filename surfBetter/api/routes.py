from flask import Blueprint, jsonify, request
from flask_praetorian import auth_required, current_user
import flask_praetorian
from extensions import guard, db
from models import User
import os

routes = Blueprint('routes',__name__)



@routes.route('/api/')
def api_hello():
    """[Default hello Api route]
    Returns:
        [Json]: [hello message]
        [Request Code]: [200 = OK]
    """
    print("hello")
    return {"HELLO": "OLA SURFISTA OLA"}, 200

@routes.route("/api/login", methods=['GET', 'POST'])
def login():
    """Logs an user in by  parsing POST request contains user credentials and iussing a JWT token response"""
    req = request.get_json(force=True)
    email = req["email"]
    password = req["password"]
    print("hello")
    if db.session.query(User).filter_by(email=email).count() == 1:
        user = guard.authenticate(email, password)
        ret = {'access_token': guard.encode_jwt_token(user)}
        return ret, 200
    else:
        return {'AutenticationError': 'Email and/or password incorrect'}, 401


@routes.route('/api/signin', methods=['POST'])
def signin():
    req = request.get_json(force=True)
    name = req["name"]
    surname = req["surname"]
    nick = req["nick"]
    email = req["email"]
    password = req["password"]

    if (nick[0] != "@"):
        nick = "@" + nick

    if db.session.query(User).filter_by(email=email).count() < 1 and \
            db.session.query(User).filter_by(nick=nick).count() < 1:
        db.session.add(
            User(
                email=email,
                name=name,
                surname=surname,
                nick=nick,
                password=guard.hash_password(password),
                roles="user",
            )
        )
        db.session.commit()
        user = guard.authenticate(email, password)

        # Create user directory
        os.makedirs("statics/user/"+nick)

        ret = {'access_token': guard.encode_jwt_token(user)}
        return ret, 200

    return {'signin_error': 'Email or nick is currently in the system'}, 401

@routes.route('/api/refresh', methods=['POST'])
def refresh():
    """Refresh token by copying all token]"""
    try:
        print("refresh request")
        new_token = guard.refresh_jwt_token(flask.request.get_data())  # instance new token by copy old token
        return {'access_token': new_token}, 200
    except Exception:
        return {'ERROR', 'Internal server error'}, 500

@routes.route('/api/current_user')
@auth_required
def current_user():
    """
    Get current loged user
    """
    user = flask_praetorian.current_user()
    return user.convert_to_json(), 200


@routes.route('/api/protected')
@auth_required
def ptotected():
    """[Simulation of auth_rqeuired. Basicly it eill required a header containing a valid JWT]"""
    current_user = db.session.query(User).filter_by(nick=f'{flask_praetorian.current_user().nick}').first()
    print(current_user)
    return "protected example", 200

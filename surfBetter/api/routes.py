from flask import Blueprint, jsonify, request
from flask_praetorian import auth_required, current_user
import flask_praetorian
from extensions import guard, db
from models import User, Beach, DescriptionPoints
import os

routes = Blueprint('routes', __name__)


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
    name = req["name"].capitalize()
    surname = req["surname"].capitalize()
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
        os.makedirs("statics/user/" + nick)

        ret = {'access_token': guard.encode_jwt_token(user)}
        return ret, 200

    return {'signin_error': 'Email or nick is currently in the system'}, 401


@routes.route('/api/refresh', methods=['POST'])
def refresh():
    """Refresh token by copying all token]"""
    try:
        print("refresh request")
        new_token = guard.refresh_jwt_token(request.get_data())  # instance new token by copy old token
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


@routes.route('/api/passwordreset', methods=['PUT'])
@auth_required
def passwordreset():
    req = request.get_json(force=True)
    user = flask_praetorian.current_user()
    if not guard.authenticate(user.email, req["old-password"]):
        return "Is this your old password ?", 428
    else:
        user.password = guard.hash_password(req["new-password"])
        return "password has been updated", 200


@routes.route('/api/userupdate', methods=['PUT'])
@auth_required
def updateUserProfile():
    """[Update user information]

    Returns:
        [httpRseponse, 409]: ["email or nick is already in use"]
        [httpResponse Json Object, 200]: ["User object"]
    """
    req = request.get_json(force=True)
    nick = req["nick"]
    email = req["email"]
    description = req["description"].capitalize()

    if nick[0] != "@":
        nick = "@" + nick

    if description == "":
        description = "I dont like descriptions"

    user = flask_praetorian.current_user()
    print(user)

    if nick != user.nick:
        newUserRoute = "statics/user/" + nick
        os.rename("statics/user/" + user.nick, newUserRoute)
        if user.avatar != "statics/default/avatar_light.png":
            newFileRoute = newUserRoute + user.get_avatar_route()[0]
            user.avatar = newFileRoute

    # First check email and nick
    if email != user.email or nick != user.nick:
        if db.session.query(User).filter_by(email=email).count() >= 1 and \
                db.session.query(User).filter_by(nick=nick).count() >= 1:
            return f"{email} or {nick} all already in use", 409

    user.name = req["name"].capitalize()
    user.surname = req["surname"].capitalize()
    user.description = description
    user.nick = nick
    user.email = email
    db.session.commit()
    return user.convert_to_json(), 200


@routes.route('/api/protected')
@auth_required
def ptotected():
    """[Simulation of auth_rqeuired. Basicly it eill required a header containing a valid JWT]"""
    current_user = db.session.query(User).filter_by(nick=f'{flask_praetorian.current_user().nick}').first()
    print(current_user)
    return "protected example", 200

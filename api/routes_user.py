from flask import Blueprint, jsonify, request
from flask_praetorian import auth_required
import flask_praetorian
from extensions import guard, db
from models import User
import os

routes_user = Blueprint('routes_user', __name__)


@routes_user.route("/api/login", methods=['GET', 'POST'])
def login():
    """
    Logs an user in by  parsing POST request contains user credentials and issuing a JWT token response
    Fields valid by user
    """
    req = request.get_json(force=True)
    email = req["email"]
    password = req["password"]
    try:
        if db.session.query(User).filter_by(email=email).count() == 1:
            user = guard.authenticate(email, password)
            ret = {'access_token': guard.encode_jwt_token(user)}
            return ret, 200
        else:
            return {'AuthenticationError': 'Email and/or password incorrect'}, 401

    except Exception as e:
        return {"Error": str(e)}, 500


@routes_user.route('/api/signin', methods=['POST'])
def sign_in():
    """
    Sign in an user by parsing POST request contains user data and using JWT token response
    Fields valid by user
    """
    req = request.get_json(force=True)
    name = req["name"].capitalize()
    surname = req["surname"].capitalize()
    nick = req["nick"]
    email = req["email"]
    password = req["password"]

    if nick[0] != "@":
        nick = "@" + nick
    try:
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

    except Exception as e:
        return {"Error": str(e)}, 500

    return {'signing_error': 'Email or nick is currently in the system'}, 401


@routes_user.route('/api/current_user')
@auth_required
def current_user():
    """Get user by flask_praetorian"""
    user = flask_praetorian.current_user()
    return user.convert_to_json(), 200


@routes_user.route('/api/passwordreset', methods=['PUT'])
@auth_required
def password_reset():
    """Reset password by flask_praetorian"""

    req = request.get_json(force=True)
    user = flask_praetorian.current_user()
    if req["old-password"] != req["new-password"]:
        try:
            guard.authenticate(user.email, req['old-password'])
            user.password = guard.hash_password(req["new-password"])
            db.session.commit()
            # ret = {'access_toke': guard.encode_jwt_token(user)}
            return jsonify("password updated"), 200
        except Exception:
            return {"Error", "password incorrect"}, 401
    else:
        return {"Error", "password is the same"}, 401


@routes_user.route('/api/userupdate', methods=['PUT'])
@auth_required
def update_user_profile():
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

    try:
        if nick != user.nick:
            new_user_route = "statics/user/" + nick + "/"
            os.rename("statics/user/" + user.nick, new_user_route)
            if user.avatar != "statics/default/avatar_light.png":
                new_file_route = new_user_route + user.get_avatar_route()[0]
                user.avatar = new_file_route

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

    except Exception as e:
        return {"Error": str(e)}, 500


@routes_user.route('/api/refresh', methods=['POST'])
@auth_required
def refresh():
    """Refresh token by copying all token"""
    try:
        print("refresh request")
        new_token = guard.refresh_jwt_token(request.get_data())  # instance new token by copy old token
        return {'access_token': new_token}, 200
    except Exception as e:
        return {'Error': str(e)}, 401
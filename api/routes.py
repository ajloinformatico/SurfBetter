from flask import Blueprint, jsonify, request
from flask_praetorian import auth_required, current_user
import flask_praetorian
from extensions import guard, db, desc
from models import User, Beach, DescriptionPoints, Likes, Comments, LikesOfComment
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
        newUserRoute = "statics/user/" + nick + "/"
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
    return "protected example", 200


@routes.route('/api/beaches/')
def get_beaches():
    """
    Get all beaches with all the data
    """
    try:
        beaches = db.session.query(Beach).all()
        beaches_list = [beach.convert_to_json() for beach in beaches]
        return jsonify(beaches_list), 200
    except:
        return jsonify("Something was wrong"), 500


@routes.route('/api/beaches/points')
def get_description_points():
    """
    Get points info
    """
    beach_points = db.session.query(DescriptionPoints).all()
    beach_points_list = [point.convert_to_json() for point in beach_points]
    return jsonify(beach_points_list), 200


@routes.route("/api/beach/<beach_id>")
def get_one_beach_info(beach_id: int):
    """
    Get only info of one beach
    """
    try:
        beach = db.session.query(Beach).filter_by(id=beach_id).first()
        return beach.convert_to_json(), 200

    except:
        return "Beach not found", 404


@routes.route('/api/beaches/coords')
def get_beaches_cords():
    """
    Get all cords of a beach
    """
    beaches = db.session.query(Beach).all()
    coords_list = [beach.get_map_info() for beach in beaches]
    return jsonify(coords_list), 200


@routes.route('/api/beach/coords/<beach_id>')
def get_one_beach_coords(beach_id: int):
    """
    Get coords of a beach
    """
    try:
        beach = db.session.query(Beach).filter_by(id=beach_id).first()
        return beach.get_map_info(), 200
    except:
        return "Beach not found", 404


@routes.route('/api/beach/filter/<name>')
def get_most_likes(name: str):
    """
    Get beaches by a query
    """
    beaches = Beach.query.filter(Beach.name.like(f'%{name}%')).all()
    print(beaches)
    beaches_list = [beach.convert_to_json() for beach in beaches]
    return jsonify(beaches_list), 200


@routes.route("/api/user/fav_comments_beches/<type>")
@auth_required
def get_profile_favorites_beaches(type: int):
    """
    Get user likes beaches
    if type == 0 return favorite beaches else most comments beaches
    """
    user_id = flask_praetorian.current_user_id()
    if int(type) == 0:
        beaches_id = db.session.query(Likes.beach_id).filter_by(user_id=user_id).all()
    elif int(type) == 1:
        beaches_id = db.session.query(Comments.beach_id).filter_by(user_id=user_id).all()
    else:
        return "not supported option", 500

    ids = [row[0] for row in beaches_id]
    beaches = db.session.query(Beach).filter(Beach.id.in_(ids)).all()
    return jsonify([beach.convert_to_json() for beach in beaches]), 200


@routes.route("/api/beach/like", methods=['POST'])
@auth_required
def add_like_beach():
    """
    Add beach like
    """
    req = request.get_json(force=True)
    beach_id = req["beach_id"]
    user_id = flask_praetorian.current_user_id()

    if db.session.query(Likes).filter_by(
            user_id=user_id,
            beach_id=beach_id
    ).count() > 0:
        return jsonify("Comment already exists"), 500

    try:
        db.session.add(
            Likes(
                user_id=user_id,
                beach_id=beach_id
            )
        )
        db.session.commit()
    except:
        return jsonify("Something was wrong"), 500

    new_like_id = db.session.query(Likes.id).filter_by(user_id=user_id, beach_id=beach_id).first()
    return jsonify(f"Like with id {new_like_id} added correctly"), 200


@routes.route("/api/beach/like", methods=['DELETE'])
@auth_required
def delete_like_beach():
    req = request.get_json(force=True)
    beach_id = req["beach_id"]
    user_id = flask_praetorian.current_user_id()
    try:
        db.session.query(Likes).filter_by(beach_id=beach_id, user_id=user_id).delete()
        db.session.commit()
    except:
        return jsonify("Something was wrong with the delete"), 500
    return jsonify(f"Like with id {beach_id} deleted success"), 200


@routes.route("/api/beach/comment", methods=['POST'])
@auth_required
def send_commentary():
    req = request.get_json(force=True)
    beach_id = req["beach_id"]
    comment = req["comment"]
    user_id = flask_praetorian.current_user_id()
    try:
        db.session.add(
            Comments(
                comment=comment,
                user_id=user_id,
                beach_id=beach_id
            )
        )
        db.session.commit()
    except:
        return "error", 500

    return get_one_beach_info(beach_id), 200


@routes.route("/api/beach/comment/delete", methods=["DELETE"])
@auth_required
def delete_comment():
    req = request.get_json(force=True)
    db.session.query(Comments).filter_by(id=req["comment_id"]).delete()
    db.session.commit()
    return f"comment with id {req['comment_id']} has been deleted", 200


@routes.route("/api/beach/comment/like", methods=["POST"])
@auth_required
def add_like_comment():
    req = request.get_json(force=True)
    comment_id = req["comment_id"]
    user_id = flask_praetorian.current_user_id()

    if db.session.query(LikesOfComment).filter_by(
            user_id=user_id,
            comment_id=comment_id
    ).count() > 0:
        return jsonify("comment already exists"), 500

    try:
        db.session.add(
            LikesOfComment(
                user_id=user_id,
                comment_id=comment_id
            )
        )
        db.session.commit()
    except:
        return jsonify("Something was wrong"), 500
    like_on_comment_id = db.session.query(LikesOfComment.id).filter_by(comment_id=comment_id, user_id=user_id).first()
    return jsonify(f"Like with id {like_on_comment_id} added success"), 200


@routes.route("/api/beach/comment/like", methods=["DELETE"])
@auth_required
def delete_like_comment():
    req = request.get_json(force=True)
    comment_id = req["comment_id"]
    user_id = flask_praetorian.current_user_id()
    try:
        db.session.query(LikesOfComment).filter_by(comment_id=comment_id, user_id=user_id).delete()
        db.session.commit()
    except:
        return jsonify("Something was wrong with the delete"), 500

    return jsonify(f"Like with id {comment_id} deleted success"), 200

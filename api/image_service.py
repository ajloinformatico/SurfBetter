from flask import Blueprint, request, send_from_directory
from models import User, Beach
from extensions import db
from flask_praetorian import auth_required, current_user
import flask_praetorian
import os

api_images = Blueprint('api_images', __name__)


@api_images.route("/api/images")
def pruena():
    return "hello to image service", 200


@api_images.route("/api/images/upload", methods=['POST'])
def upload_image():
    if (request.method == "POST"):
        file = request.files['file']
        try:
            # os.getcwd() -> return actual directory
            file.save(os.getcwd() + "/img/" + file.filename)
            return "Guardado", 200

        except FileNotFoundError:
            return "El archivo no existe", 400


@api_images.route("/api/avatar", methods=['PUT', 'GET'])
@auth_required
def get_avatar():
    """[Update or get avatar image]:
    Args:
        filename ([file]): [Image to update]

    Returns:
        [file response]: [return user image]
    """
    user = flask_praetorian.current_user()
    file_route_original = user.get_avatar_route()
    # if request method get just get user image
    if request.method == "GET":
        try:
            print(file_route_original[1], file_route_original[0])
            return send_from_directory(os.getcwd() + file_route_original[1], filename=file_route_original[0],
                                       as_attachment=False), 200
        except:
            return "Something was wrong with the file or route", 500
    elif request.method == "PUT":
        try:
            file = request.files['file']
            user_db = db.session.query(User).filter_by(nick=f'{user.nick}').first()

            # check if new image is diferent than the original
            if file.filename != file_route_original[0]:
                new_route = os.getcwd() + "/statics/user/" + user.nick + "/"
                # save new image 
                file.save(new_route + file.filename)

                # check if route isnt the default to delete old avatar
                if file_route_original[1] != "/statics/default/":
                    os.remove(os.getcwd() + user.avatar)

                user_db.avatar = "/statics/user/" + user.nick + "/" + file.filename
                db.session.commit()

                # Get updated routes to return new user avatar
                file_route_original = user_db.get_avatar_route()

            return send_from_directory(os.getcwd() + file_route_original[1], filename=file_route_original[0],
                                       as_attachment=False), 200
        except FileNotFoundError:
            return "the file do not exists", 400


@api_images.route('/api/beach/image/<beach_id>', methods=["GET"])
def get_beach_mage(beach_id: int):
    """
    Get beach image
    """
    try:
        beach = db.session.query(Beach).filter_by(id=beach_id).first()
        beach = beach.convert_to_json()
        prepare_route = beach["image"].split("/")
        file_name = prepare_route.pop(-1)
        file_route = "/".join(prepare_route) + "/"
        print(file_name, file_route)
        return send_from_directory(os.getcwd() + file_route, filename=file_name, as_attachment=False), 200
    except Exception:
        return "File not found", 400
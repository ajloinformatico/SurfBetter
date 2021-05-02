from flask import Blueprint, request, send_from_directory
import os

api_images = Blueprint('api_images', __name__)

@api_images.route("/api/images")
def pruena():
    return "Hola",200


@api_images.route("/api/images/upload", methods=['POST'])
def upload_image():
    if (request.method == "POST"):
        file = request.files['file']
        try:
            # os.getcwd() -> return actual directory
            file.save(os.getcwd() + "/img/"+file.filename)
            return "Guardado",200

        except FileNotFoundError:
            return "El archivo no existe", 400

@api_images.route("/images/<string:filename>")
def get_image(filename):
    return send_from_directory(os.getcwd() + "/img/", filename=filename, as_attachment=False)
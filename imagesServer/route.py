from flask import Blueprint

api_images = Blueprint('api_images', __name__)

# Continuae by https://www.youtube.com/watch?v=pOFEjJ7NQek 4.35
api_images.route("/")
def pruena():
    return "Hola",200
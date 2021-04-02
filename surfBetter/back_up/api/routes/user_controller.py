from flask import Blueprint, jsonify, request

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/user', methods=['GET'])
def get_all_users():
    """
    Get all users
    Returns: json all users
    """
    return jsonify({'status': '200', 'message': 'it will return all users'})


@user_routes.route("/login", methods=['POST'])
def login():
    """
    check user
    Returns:

    """
    req = request.get_json(force="True")
    name = req.get("name", None)
    surname = req.get("surname", None)
    nick = req.get("nick", None)
    email = req.get("email", None)
    password = req.get("password", None)
    print(name, surname)



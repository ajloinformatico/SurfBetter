from flask import Blueprint, jsonify, request

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/user', methods=['GET'])
def get_all_users():
    """
    Get all users
    Returns: json all users
    """
    return jsonify({'status': '200', 'message': 'it will return all users'})


@user_routes.route("/user/login", methods=['POST'])
def login():
    """
    check user
    Returns:

    """
    data = request.get_json()
    print(data)
    return data



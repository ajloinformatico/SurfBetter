from flask import Flask, Blueprint, jsonify

from . import db

auth = Blueprint('auth', __name__)


@auth.route('/user', methods=['GET'])
def signup():
    return jsonify({'status': '200', 'message': 'it will return all users'})

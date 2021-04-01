from flask import Blueprint
from app import db
from flask_bcrypt import Bcrypt
from werkzeug.security import safe_str_cmp

app_models = Blueprint('app_models', __name__)


# auth : https://yasoob.me/posts/how-to-setup-and-deploy-jwt-auth-using-react-and-flask/
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=False)
    # roles = db.Column(db.String)
    # is_active = is_active = db.Column(db.Boolean, default=True, server_default='true')
    nick = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(130), unique=True, nullable=False)
    avatar = db.Column(db.String, unique=True, nullable=True)
    password_hash = db.Column(db.String(64), nullable=False)

    def set_password(self, password):
        """
        Set password
        Args:
            password: {String} user password

        Returns: {Void} just set user password

        """
        if len(password) < 8:
            raise ValueError("Error : password must have almost 8 characters")
        self.password_hash = Bcrypt.generate_password_hash(password)

    def check_password(self, password):
        """
        Check correct password
        Args:
            password: {String} user password

        Returns: {Bool} : password correct

        """
        return Bcrypt.check_password_hash(password, self.password_hash)

    def __repr__(self):
        return self.username

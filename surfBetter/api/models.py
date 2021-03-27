from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from werkzeug.security import safe_str_cmp

app = Flask(__name__)
bcrypt = Bcrypt(app)  # password
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/surfbetter.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    nick = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(30), nullable=False)

    def set_password(self, password):
        """
        Set password
        Args:
            password: {String} user password

        Returns: {Void} just set user password

        """
        if len(password) < 8:
            raise ValueError("Error : password must have almost 8 characters")
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        """
        Check correct password
        Args:
            password: {String} user password

        Returns: {Bool} : password correct

        """
        return bcrypt.check_password_hash(password, self.password_hash)


    def __repr__(self):
        return self.username

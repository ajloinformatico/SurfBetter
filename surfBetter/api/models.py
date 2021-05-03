from extensions import db
from flask import jsonify
class User(db.Model):
    """User model
    Args:
        db (SQLAlchemy model): [SQLAlchemy ORM database]
    """

    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.String(63), unique=False, nullable=False)
    surname = db.Column(db.String(63), unique=False, nullable=False)
    avatar = db.Column(db.Text, unique=False, nullable=True, server_default='statics/default/avatar_light.png')
    nick = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(63), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True, server_default='Hello there ! I`m using SurfBetter')
    roles = db.Column(db.String(10))
    is_active = db.Column(db.Boolean, default=True, server_default='true')

    @property
    def identity(self):
        """[Get user id]
        Returns:
            [int]: [User id]
        """
        return self.id

    @property
    def rolenames(self):
        """[Generate property to return the roles of a user separated by commas]
        Returns:
            [List]: [User comma separated roles]
        """
        try:
            return self.roles.split(",")
        except Exception:
            return []

    @classmethod
    def lookup(cls, email):
        """[Get a player by email]
        Args:
            email (str): [email  to lookup]
        Returns:
            [User]: [User lookup]
        """
        return cls.query.filter_by(email=email).one_or_none()

    @classmethod
    def identify(cls, id):
        """[get user id]
        Returns:
            [int]: [User id]
        """
        return cls.query.get(id)

    def convert_to_json(self):
        """
        Returns: [dic]: User json
        """
        return jsonify(
            id=self.id,
            name=self.name,
            surname=self.surname,
            avatar=self.avatar,
            nick=self.nick,
            description=self.description
        )
    
    def get_avatar_route(self):
        """[return avatar image name and route ]
        """
        avatar_route = self.avatar.split("/")
        return (avatar_route.pop(-1), "/"+"/".join(avatar_route)+"/")

    def is_valid(self):
        """[Check if an user is active on the app]
        Returns:
            [bool]: [if user active]
        """
        return self.is_active

    def __repr__(self):
        """
        Not neceesary i use it for sqlite console
        TODO: CONTINUE HERE AND SET ON PROFILE
        """
        return '<User %r,%r,%r,%r,%r,%r>' % (self.email, self.name, self.surname, self.nick, self.password, self.roles)




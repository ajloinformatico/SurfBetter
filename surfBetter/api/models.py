from extensions import db
from flask import jsonify
import datetime


class User(db.Model):
    """[User model]
        RelationShips:
            1:1 with likesOfComment
            1:M with Comments
            1:M With Likes
    Args:
        db (SQLAlchemy model): [SQLAlchemy ORM database]
    """

    __tablename__ = "user"

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
    #RelationShips
    #1:1 likesOfComment
    likes_on_comments = db.relationship("LikesOfComment", uselist=False, back_populates="user")
    #1:M Comments
    comments = db.relationships("Comments", backref='user', lazy=True)
    #1:M Likes
    likes = db.relationships("Likes", backref='user', lazy=True)



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
            email=self.email,
            name=self.name,
            surname=self.surname,
            avatar=self.avatar,
            nick=self.nick,
            password=self.password,
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


# TODO: if i get it from api set flag by enum type
class beach(db.Model):
    """[Beach model]
        Relationships:
        1:M With Comments
        1:M With Likes

    Args:
        db ([sqlAlchemy]): [sqlAlchemy instance]
    """
    __tablename__ : "beach"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    image = db.Column(db.String, unique=True, nullable=False)
    type = db.Column(db.String, nullable=False)
    #Foreign keys
    comments = db.relationship("Comments", backref='beach', lazy=True)
    likes = db.relationship("Likes", backref='beach', lazy=True)



    def __repr__(self):
        return "<Beach %r,%r,%r>" % (self.id, self.name, self.image, self.type)
    

class Comments(db.Model):
    """[Comments]
        RelationShips:
        1:M With LikesOfComments
        M:1 With User
        M:1 With Beach


    Args:
        db ([sqlAlchemy]): [sqlAlchemy instance]
    """
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # Foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    beach_id = db.Column(db.Integer, db.ForeignKey("beach.id"), nullable=False)

    #RelationShips
    #(in 1: m relations it is not necessary to make the relation to others one's own foreign)
    Likes_of_comment = db.relationship("LikesOfComment", back_populates="comments")



    def __repr__(self):
        return "<Comment %r,%r,%r>" % (self.id, self.comment, self.created_date)



class Likes(db.Model):
    """[Likes Models]
        RelationsShips:
        M:1 With User
        M:1 With Beach
        

    Args:
        db ([sqlAlchemy]): [sqlAlchemy instance]
    """
    __tablename__ = "likes"

    id = db.Column(db.Integer, ptimary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    beach_id = db.Column(db.Integer, db.ForeignKey("beach.id"), nullable=False)

    def __repr__(self):
        return "<Likes %r,%r>" % (self.id, self.created_date)        
    

class LikesOfComment(db.Model):
    """[Class for the likes on the coments]
        RelationShips:
        1:1 Wiht User
        1:M With Comments

    Args:
        db ([sqlAlchemy]): [sqlALCHEMY]
    """
    __tablename__ = "likes_of_comment"

    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False)
    #RelationShips (1:m no need relation atribute)
    #1:1 With User
    user = db.relationship("User", back_populates="likes_of_comment")

    def __repr__(self):
        return "<Likes %r,%r" % (self.id, self.created_date)

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
        db.Model (SQLAlchemy model): [SQLAlchemy ORM database]
    """

    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}

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
    # RelationShips
    # 1:1 likesOfComment
    likes_on_comments = db.relationship("LikesOfComment", uselist=False, backref='user')
    # 1:M Comments
    comments = db.relationship("Comments", backref='user', lazy=True)
    # 1:M Likes
    likes = db.relationship("Likes", backref='user', lazy=True)

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
        # TODO CHECK WITHOUT ONE /
        return avatar_route.pop(-1), "/" + "/".join(avatar_route) + "/"

    def is_valid(self):
        """[Check if an user is active on the app]
        Returns:
            [bool]: [if user active]
        """
        return self.is_active

    def __repr__(self):
        return '<User %r,%r,%r,%r,%r,%r>' % (self.email, self.name, self.surname, self.nick, self.password, self.roles)


def get_comments_from_beach(beach_id: int):
    list_of_comment = []
    comments = db.session.query(Comments).filter_by(beach_id=beach_id).all()
    for comment in comments:
        list_of_comment.append(comment.convert_to_json())
    return {"comments": comments}


class Beach(db.Model):
    """[Beach model]
        Relationships:
        1:M With Comments
        1:M With Likes

        flags = 0 : red | 1: orange | 2: yellow | 3: green
        wave_secuence, wave_height, tidies, weend_speed | 1, 2, 3, 4, 5

        onCardView: quality_when_it_works, wave_Consistency, difficulty, windsurf_y_kitesurf
                    people_to_water, general and user_rating check it on the client



    Args:
        db.Model ([sqlAlchemy]): [sqlAlchemy instance]
    """
    __tablename__ = "beach"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    image = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.Text)
    type_beach = db.Column(db.String, nullable=False)
    flag = db.Column(db.Integer, nullable=False)
    quality_when_it_works = db.Column(db.Integer, nullable=False)
    wave_consistency = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)
    windsurf_y_kitesurf = db.Column(db.Integer, nullable=False)
    people_to_water = db.Column(db.Integer, nullable=False)
    # Other points on the detail view
    sea_weends = db.Column(db.String, nullable=True, server_default=None)
    other_options = db.Column(db.Integer, nullable=True, server_default=None)
    water_quality = db.Column(db.Integer, nullable=True, server_default=None)
    access = db.Column(db.Integer, nullable=True, server_default=None)
    scenery = db.Column(db.Integer, nullable=True, server_default=None)
    local_attitude = db.Column(db.Integer, nullable=True, server_default=None)
    accommodation = db.Column(db.Integer, nullable=True, server_default=None)
    camping = db.Column(db.Integer, nullable=True, server_default=None)
    entertainment = db.Column(db.Integer, nullable=True, server_default=None)
    equipment_and_repairs = db.Column(db.Integer, nullable=True, server_default=None)
    restaurants = db.Column(db.Integer, nullable=True, server_default=None)
    pubs = db.Column(db.Integer, nullable=True, server_default=None)
    # surfForescastLink
    surf_fore_cast_link = db.Column(db.String, nullable=False)
    # map location
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    # Foreign keys
    comments = db.relationship("Comments", backref='beach', lazy=True)
    likes = db.relationship("Likes", backref='beach', lazy=True)

    def convert_to_json(self):
        """
        Return Json of the object
        """
        return {"id": self.id, "name": self.name, "image": self.image, "description": self.description,
                "type_beach": self.type_beach, "falg": self.flag, "quality_when_it_works": self.quality_when_it_works,
                "wave_consistency": self.wave_consistency, "difficulty": self.difficulty,
                "windsurf_y_kitesurf": self.windsurf_y_kitesurf, "people_to_water": self.people_to_water,
                "sea_weends": self.sea_weends, "other_options": self.other_options, "water_quality": self.water_quality,
                "access": self.access, "scenery": self.scenery, "local_attitude": self.local_attitude,
                "accommodation": self.accommodation, "camping": self.camping, "entertainment": self.entertainment,
                "equipment_and_repairs": self.equipment_and_repairs, "restaurants": self.restaurants, "pubs": self.pubs,
                "surf_fore_cast_link": self.surf_fore_cast_link, "latitude": self.latitude, "longitud": self.longitude,
                "comments": [comment.convert_to_json() for comment in self.comments],
                "likes": [likes.convert_to_json() for likes in self.likes]
                }

    def get_map_info(self):
        """
        Return map data
        """
        return {
            "id": self.id,
            "name": self.name,
            "latitude": self.latitude,
            "longitude": self.longitude
        }

    def __repr__(self):
        return "<Beach %r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r>" % \
               (
                   self.id, self.name, self.image, self.description, self.type_beach, self.flag,
                   self.quality_when_it_works,
                   self.wave_consistency, self.difficulty, self.windsurf_y_kitesurf, self.people_to_water,
                   self.sea_weends,
                   self.other_options, self.water_quality, self.access, self.scenery, self.local_attitude,
                   self.accommodation,
                   self.camping, self.entertainment, self.equipment_and_repairs, self.restaurants,
                   self.pubs, self.surf_fore_cast_link, self.latitude, self.longitude, self.comments,
                   self.likes
               )


class DescriptionPoints(db.Model):
    """[Beaches description model]

    Args:
        db.Model (database): [mysqlAlchemy instance]
    """
    __tablename__ = "description_points"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    point_info = db.Column(db.Text)

    def convert_to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "point_info": self.point_info
        }

    def __repr__(self):
        return "<Description Points %r,%r,%r>" % (self.id, self.name, self.point_info)


class Comments(db.Model):
    """[Comments]
        RelationShips:
        1:M With LikesOfComments
        M:1 With User
        M:1 With Beach


    Args:
        db.Model ([sqlAlchemy]): [sqlAlchemy instance]
    """
    __tablename__ = "comments"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(300), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # Foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    beach_id = db.Column(db.Integer, db.ForeignKey("beach.id"), nullable=False)

    # RelationShips
    # (in 1: m relations it is not necessary to make the relation to others one's own foreign)
    likes_of_comment = db.relationship("LikesOfComment", backref="comments", lazy=True)

    def __repr__(self):
        return "<Comment %r,%r,%r,%r>" % (self.id, self.comment, self.created_date, self.likes_of_comment)

    def convert_to_json(self):
        return {"id": self.id, "comment": self.comment, "created_date": self.created_date, "user_id": self.user_id, "beach_id": self.beach_id,
                "likes_of_comments": [likes_of_c.convert_to_json() for likes_of_c in self.likes_of_comment]}


class Likes(db.Model):
    """[Likes Models]
        RelationsShips:
        M:1 With User
        M:1 With Beach
        

    Args:
        db.Model ([sqlAlchemy]): [sqlAlchemy instance]
    """
    __tablename__ = "likes"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    beach_id = db.Column(db.Integer, db.ForeignKey("beach.id"), nullable=False)

    def convert_to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "created_date": self.created_date,
            "beach_id": self.beach_id
        }

    def __repr__(self):
        return "<Likes %r,%r>" % (self.id, self.created_date)


class LikesOfComment(db.Model):
    """[Class for the likes on the coments]
        RelationShips:
        1:1 Wiht User
        1:M With Comments

    Args:
        db.Model ([sqlAlchemy]): [sqlALCHEMY]
    """
    __tablename__ = "likes_of_comment"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable=False)


    def convert_to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "comment_id": self.comment_id,
            "created_date": self.created_date
        }

    def __repr__(self):
        return "<Likes %r,%r" % (self.id, self.created_date)

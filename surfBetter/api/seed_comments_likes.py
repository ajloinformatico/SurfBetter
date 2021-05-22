from models import Likes, Comments, LikesOfComment
from extensions import db


def seed_likes(app):
    with app.app_context():
        if db.session.query(Likes).count() < 1:
            db.session.add_all(
                [
                    Likes(
                        id=1,
                        user_id=1,
                        beach_id=12
                    ),
                    Likes(
                        id=2,
                        user_id=1,
                        beach_id=9
                    ),
                    Likes(
                        id=3,
                        user_id=1,
                        beach_id=2
                    ),
                    Likes(
                        id=4,
                        user_id=2,
                        beach_id=12
                    ),
                    Likes(
                        id=5,
                        user_id=2,
                        beach_id=9
                    ),
                    Likes(
                        id=6,
                        user_id=3,
                        beach_id=4,
                    ),
                    Likes(
                        id=7,
                        user_id=3,
                        beach_id=20
                    ),
                    Likes(
                        id=8,
                        user_id=3,
                        beach_id=12
                    ),
                    Likes(
                        id=9,
                        user_id=3,
                        beach_id=20
                    ),
                    Likes(
                        id=10,
                        user_id=4,
                        beach_id=1
                    ),
                    Likes(
                        id=12,
                        user_id=4,
                        beach_id=40,
                    ),
                    Likes(
                        id=13,
                        user_id=4,
                        beach_id=12
                    ),
                    Likes(
                        id=14,
                        user_id=5,
                        beach_id=12
                    ),
                    Likes(
                        id=15,
                        user_id=5,
                        beach_id=6
                    ),
                    Likes(
                        id=16,
                        user_id=5,
                        beach_id=31
                    )
                ]
            )
            db.session.commit()


def seed_comments(app):
    with app.app_context():
        if db.session.query(Comments).count() < 1:
            db.session.add_all(
                [
                    Comments(
                        id=1,
                        comment="No idea of surfing but it was cool",
                        user_id=2,
                        beach_id=12
                    ),
                    Comments(
                        id=2,
                        comment="Good place to do kaisurf",
                        user_id=2,
                        beach_id=9
                    ),
                    Comments(
                        id=3,
                        comment="Great moments with my girl a camera and a table",
                        user_id=1,
                        beach_id=2
                    ),
                    Comments(
                        id=4,
                        comment="An inflatable boat, food and many waves",
                        user_id=2,
                        beach_id=1
                    ),
                    Comments(
                        id=5,
                        comment="A good place to catch waves",
                        user_id=3,
                        beach_id=12
                    ),
                    Comments(
                        id=6,
                        comment="Just fantastic",
                        user_id=2,
                        beach_id=2
                    ),
                    Comments(
                        id=7,
                        comment="No idea of surfing but it was cool",
                        user_id=2,
                        beach_id=12
                    ),
                    Comments(
                        id=8,
                        comment="si hay sol hay playa si hay playa hay alchol ..",
                        user_id=3,
                        beach_id=20
                    ),
                    Comments(
                        id=9,
                        comment="I tried windsurfing and a great idea",
                        user_id=4,
                        beach_id=30
                    ),
                    Comments(
                        id=10,
                        comment="si hay sol hay playa si hay playa hay alchol ..",
                        user_id=3,
                        beach_id=20
                    ),
                    Comments(
                        id=11,
                        comment="I couldn't catch waves a bad idea to go :(",
                        user_id=5,
                        beach_id=6
                    ),
                    Comments(
                        id=12,
                        comment="in the end we did nothing but highly recommended",
                        user_id=4,
                        beach_id=14
                    ),
                    Comments(
                        id=13,
                        comment="a damn beach pass my god what a locuron",
                        user_id=5,
                        beach_id=31
                    ),
                ]
            )
            db.session.commit()


def seed_likes_of_comment(app):
    with app.app_context():
        if db.session.query(LikesOfComment).count() < 1:
            db.session.add_all(
                [
                    # todo seeder likes of comments
                    LikesOfComment(
                        user_id=1,
                        comment_id=5
                    ),
                    LikesOfComment(
                        user_id=1,
                        comment_id=10
                    ),
                    LikesOfComment(
                        user_id=1,
                        comment_id=3
                    ),
                    LikesOfComment(
                        user_id=2,
                        comment_id=12,
                    ),
                    LikesOfComment(
                        user_id=2,
                        comment_id=3
                    ),
                    LikesOfComment(
                        user_id=2,
                        comment_id=1
                    ),
                    LikesOfComment(
                        user_id=3,
                        comment_id=11,
                    ),
                    LikesOfComment(
                        user_id=3,
                        comment_id=9
                    ),
                    LikesOfComment(
                        user_id=3,
                        comment_id=4
                    ),
                    LikesOfComment(
                        user_id=4,
                        comment_id=10
                    ),
                    LikesOfComment(
                        user_id=4,
                        comment_id=5,
                    ),
                    LikesOfComment(
                        user_id=4,
                        comment_id=1
                    ),
                    LikesOfComment(
                        user_id=5,
                        comment_id=12
                    ),
                    LikesOfComment(
                        user_id=5,
                        comment_id=13
                    ),
                    LikesOfComment(
                        user_id=5,
                        comment_id=2
                    )
                ]
            )
            db.session.commit()
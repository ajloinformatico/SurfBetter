from models import User
from extensions import db


def seed(app):
    """
    Make seeder if it is necessary
    """
    with app.app_context():
        db.create_all()
        if db.session.query(User).filter_by(email="ajloinformatico@gmail.com").count() < 1:
            db.session.add(
                User(
                    email="ajloinformatico@gmail.com",
                    name="Infolojo",
                    surname="Infolojo",
                    nick="@infolojo",
                    password=guard.hash_password("pestillo01"),
                    roles="admin",
                )
            )
            db.session.commit()
        print("user exists")
from models import User, Beach, DesciptionPoints
from extensions import db, guard
import os


def createUserDirectory(nicks: list):
    for nick in nicks:
        print(nick)
        if not os.path.isdir(f"statics/user/{nick}"):
            os.makedirs(f"statics/user/{nick}")


def seedUser(app):
    """
    Make seeder if it is necessary
    """
    with app.app_context():
        db.create_all()
        if db.session.query(User).filter_by(email="ajloinformatico@gmail.com").count() < 1:
            db.session.add_all(
                [
                    User(
                        email="ajloinformatico@gmail.com",
                        name="Infolojo",
                        surname="Infolojo",
                        nick="@infolojo",
                        password=guard.hash_password("pestillo01"),
                        roles="admin",
                    ),
                    User(
                        email="javierortegans@gmail.com",
                        name="Javier",
                        surname = "Ortega",
                        nick="@javier",
                        password=guard.hash_password("pestillo01"),
                        roles="user",
                    ),
                    User(
                        email="javiergonzalez@gmail.com",
                        name="Javier",
                        surname = "Gonzalez",
                        nick="@javier2",
                        password=guard.hash_password("pestillo01"),
                        roles="user",
                    ),
                    User(
                        email="marina@gmail.com",
                        name="Marina",
                        surname = "Miriam",
                        nick="@marina",
                        password=guard.hash_password("pestillo01"),
                        roles="user",
                    ),
                    User(
                        email="aliciamaria@hotmail.com",
                        name="alicia",
                        surname = "Lojo",
                        nick="@alicia",
                        password=guard.hash_password("pestillo01"),
                        roles="user",
                    )
                ]
            )

            db.session.commit()

            createUserDirectory(nicks=["@javier","@javier2","@marina","@alicia"])



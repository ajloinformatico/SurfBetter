from flask_sqlalchemy import SQLAlchemy
from flask_praetorian import Praetorian

db = SQLAlchemy()
desc = db.desc
guard = Praetorian()
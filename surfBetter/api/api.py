import json
import flask
import flask_sqlalchemy
import flask_praetorian
import flask_cors

db = flask_sqlalchemy.SQLAlchemy() # ORM
guard = flask_praetorian.Praetorian() # Auth JWT
cors = flask_cors.CORS() # allow requests (develop)

# User Model
class User(db.Model):
    """User model

    Args:
        db (SQLAlchemy model): [SQLAlchemy ORM database]
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.String(63), unique=False, nullable=False)
    surname = db.Column(db.String(63), unique=False, nullable=False)
    nick = db.Column(db.Text, unique=True, nullable=False)
    password =  db.Column(db.Text, unique=False, nullable=False)
    roles = db.Column(db.Text)
    is_active= db.Column(db.Boolean, default=True, server_default='true')

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
        return '<User %r,%r>' % (self.email, self.name)
    

# intialize flask basic conf & basic conf
app = flask.Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'top secret'
    
app.config['JWT_ACCESS_LIFESPAN'] = {'hours' : 24}
app.config['JWT_REFRESH_LIFESPAN'] = {'days' : 30}

# flask pretorian initialize (app, model)
guard.init_app(app, User)

# initialize sqlite database TODO IF FAILS CHANGE TO SIMETHINF LIKE THAT : app.config['SQLALCHEMY_DATABASE_URI'] = F"sqlite:///{os.path.join(os.getcwd(), 'database.db')}"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database/database.db"
db.init_app(app)

# initialize cors to debug
cors.init_app(app)

# SEEDER if not exists user admin create database and admin 
with app.app_context():
    db.create_all()
    if db.session.query(User).filter_by(email="ajloinformatico@gmail.com").count() < 1:
        print("\n\ncreate user\n\n")
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



# Example Routes
@app.route('/api/')
def api_hello():
    """[Default hello Api route]

    Returns:
        [Json]: [hello message]
        [Request Code]: [200 = OK]
    """
    return {"HELLO": "OLA SURFISTA OLA"}, 200


@app.route('/api/login', methods=['POST'])
def login():
    """Logs an user in by  parsing POST request contains user credentials and iussing a JWT token response"""
    req = flask.request.get_json(force=True)
    email = req["email"]
    password = req["password"]
    print("hello")
    if db.session.query(User).filter_by(email=email).count() == 1:
        user = guard.authenticate(email, password)
        ret = {'access_token': guard.encode_jwt_token(user)}
        return ret, 200
    else:
        return {'AutenticationError' : 'Email and/or password incorrect'}, 401

@app.route('/api/signin', methods=['POST'])
def signin():

    req = flask.request.get_json(force=True)
    name = req["name"]
    surname = req["surname"]
    nick = req["nick"]
    email = req["email"]
    password = req["password"]

    if(name[0] != "@"):
        name = "@"+name
    

    if db.session.query(User).filter_by(email=email).count() < 1 and \
        db.session.query(User).filter_by(nick=nick).count() < 1:
        db.session.add(
            User(
                email=email,
                name=name,
                surname=surname,
                nick=nick,
                password=guard.hash_password(password),
                roles="user",
            )
        )
        db.session.commit()
        user = guard.authenticate(email, password)
        ret = {'access_token':guard.encode_jwt_token(user)}
        return ret, 200
    
    return {'signin_error' : 'Email or nick is currently in the system'}, 401


# TODO: IF NOT FOUND send 401   
# return {'ERROR': email}, 401
@app.route('/api/refresh', methods=['POST'])
def refresh():
    """Refresh token by copying all token]"""
    try:
        print("refresh request")
        new_token = guard.refresh_jwt_token(flask.request.get_data()) # instance new token by copy old token
        return {'access_token': new_token}, 200
    except Exception:
        return {'ERROR', 'Internal server error'}, 500


@app.route('/api/protected')
@flask_praetorian.auth_required
def ptotected():
    """[Simulation of auth_rqeuired. Basicly it eill required a header containing a valid JWT]"""
    # current_user = db.session.query(User).filter_by(nick=f'{flask_praetorian.current_user().nick}').first()
    # print(current_user)
    user = flask_praetorian.current_user()
    print(user)
    return {"message":f"yeu"}

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


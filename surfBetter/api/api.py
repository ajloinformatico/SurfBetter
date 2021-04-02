import os
import flask
import flask_sqlalchemy
import flask_praetorian
import flask_cors

db = flask_sqlalchemy.SQLAlchemy() # ORM
guard = flask_praetorian.Praetorian() # Auth JWT
CORS = flask_cors.CORS() # allow requests (develop)

# User Model
class User(db.Model):
    """User model

    Args:
        db (SQLAlchemy model): [SQLAlchemy ORM database]
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(64), unique=False, nullable=False)
    surname = db.Column(db.Text(64), unique=False, nullable=False)
    nick = db.Column(db.Text(30), unique=True, nullable=False)
    password =  db.Column(db.Text(30), unique=False, nullable=False)
    email = db.Column(db.Text(130), unique=True, nullable=False)
    roles = db.Column(db.Text)
    is_activate = db.Column(db.Boolean, default=True, server_default='True')

    @property
    def rolenames(self):
        """[Generate property to return the roles of a user separated by commas] 

        Returns:
            [List]: [User comma separated roles]
        """
        try:
            return self.roles.split(',')
        except Exception:
            return []
    
    @classmethod
    def lookup(cls, type, param):
        """[Get a player by nick or email] 

        Args:
            type (str): 'email' or 'nick' to especify the attr to do lookup
            param (str): [nick or email  to lookup]

        Returns:
            [User]: [User lookup]
        """
        if type == 'nick':
            return cls.query.filter_by(nick=param).one_or_none()
        else:
            return cls.query.filter_by(email=param).one_or_none()

    @classmethod
    def identity(cls, id):
        """[get user id]

        Returns:
            [int]: [User id]
        """
        return cls.query.get(id)

    @property
    def identify(self):
        """[Get user id]

        Returns:
            [int]: [User id]
        """
        return self.id

    def is_valid(self):
        """[Check if an user is active on the app]
        Returns:
            [bool]: [if user active]
        """
        return self.is_activate
    

# intialize flask basic conf & basic conf
app = flask.Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'LR7aiJZO$n@~Tfmts((W)_ncOg[okufXps8[|]3?BdmtjsIiB0qCTv]fMm]Dy'
    
app.config['JWT_ACCESS_LIFESPAN'] = {'hours' : 1}
app.config['JWT_REFRESH_LIFESPAN'] = {'days' : 1}

# flask pretorian initialize (app, model)
guard.init_app(app, User)

# initialize sqlite database TODO IF FAILS CHANGE TO SIMETHINF LIKE THAT : app.config['SQLALCHEMY_DATABASE_URI'] = F"sqlite:///{os.path.join(os.getcwd(), 'database.db')}"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/surfBetter.db'
db.init_app(app)

# initialize cors to debug
CORS.init_app(app)

# SEEDER if not exists user admin create database and admin 
with app.app_context():
    db.create_all()
    if db.session.query(User).filter_by(nick='@infolojo').count() < 1:
        db.session.add(User(
            name='Infolojo',
            surname='Infolojo',
            nick="@infolojo",
            password=guard.hash_password('pestillo01'),
            email='ajloinformatico@gmail.com',
            roles='admin'
        
        ))
    db.session.commit()

# Example Routes
@app.route('/api/')
def api_hello():
    """[Default hello Api route]

    Returns:
        [Json]: [hello message]
        [Request Code]: [200 = OK]
    """
    return {"HELLO": "SURFBETTER API RUNING"}, 200


@app.route('/api/login', methods=['POST'])
def login():
    """Logs an user in by  parsing POST request contains user credentials and iussing a JWT token response"""
    req = flask.request.get_json(force=True)
    email = req.get('email', None)
    password = req.get('password', None)
    if (db.session.query(User).filter_by(email=email).count() > 1):
        user = guard.authenticate(email, password)
        res = {'access_token': guard.encode_jwt_token(user)}
        return res, 200
    
    return {'ERROR': email}, 401


@app.route('/api/refresh', methods=['POST'])
def refresh():
    """Refresh token by copying all token]"""
    try:
        print("refresh request")
        new_token = guard.refresh_jwt_token(flask.request.get_data()) # instance new token by copy old token
        return {'access_token': new_token}, 200
    except Exception:
        return {'ERROR', 'Internal server error'}, 500


@app.route('/api/profile')
@flask_praetorian.auth_required
def ptotected():
    """[Simulation of auth_rqeuired. Basicly it eill required a header containing a valid JWT]"""
    return {"message":f"protected endpoint (allowed user {flask_praetorian.current_user().nick})"}

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


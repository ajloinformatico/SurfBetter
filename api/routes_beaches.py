from flask import Blueprint, jsonify, render_template
from flask_praetorian import auth_required
import flask_praetorian
from extensions import db
from models import Beach, DescriptionPoints, Likes, Comments, LikesOfComment

routes_beaches = Blueprint("routes_beaches", __name__)


@routes_beaches.route('/api/beaches/')
def get_beaches():
    """Get all beaches with all the data"""
    try:
        beaches = db.session.query(Beach).all()
        beaches_list = [beach.convert_to_json() for beach in beaches]
        return jsonify(beaches_list), 200
    except Exception as e:
        return {"Error": str(e)}, 500

@routes_beaches.route('/api/beaches/points')
def get_description_points():
    """Get points info"""
    try:
        beach_points = db.session.query(DescriptionPoints).all()
        beach_points_list = [point.convert_to_json() for point in beach_points]
        return jsonify(beach_points_list), 200
    except Exception as e:
        return {"Error": str(e)}, 500


@routes_beaches.route("/api/beach/<beach_id>")
def get_one_beach_info(beach_id: int):
    """Get only info of one beach"""
    try:
        if db.session.query(Beach).filter_by(id=beach_id).count() < 1:
            return {"Error": "Beach not found"}, 404

        beach = db.session.query(Beach).filter_by(id=beach_id).first()
        return beach.convert_to_json(), 200

    except Exception as e:
        return {"Error": str(e)}, 500

@routes_beaches.route('/api/beaches/coords')
def get_beaches_cords():
    """Get all cords of a beach"""
    try:
        beaches = db.session.query(Beach).all()
        coords_list = [beach.get_map_info() for beach in beaches]
        return jsonify(coords_list), 200
    except Exception as e:
        return {"Error": str(e)}, 500

@routes_beaches.route('/api/beach/coords/<beach_id>')
def get_one_beach_coords(beach_id: int):
    """Get coords of a beach"""
    try:
        if (db.session.query(Beach).filter_by(id=beach_id).count() < 1):
            return {"Error", "Beach not found"}, 404

        beach = db.session.query(Beach).filter_by(id=beach_id).first()
        return beach.get_map_info(), 200
    except Exception as e:
        return {"Error": str(e)}, 500

@routes_beaches.route('/api/beach/filter/<name>')
def search_beach(name: str):
    """Get beaches by a query"""
    try:
        beaches = Beach.query.filter(Beach.name.like(f'%{name.lower()}%')).all()
        print(beaches)
        beaches_list = [beach.convert_to_json() for beach in beaches]
        return jsonify(beaches_list), 200
    except Exception as e:
        return {"Error", str(e)}, 500


@routes_beaches.route("/api/user/fav_comments_beches/<type>")
@auth_required
def get_profile_favorites_beaches(type: int):
    """
    Get user likes beaches if type == 0 return favorite beaches else most comments beaches"""
    try:
        user_id = flask_praetorian.current_user_id()
        if int(type) == 0:
            beaches_id = db.session.query(Likes.beach_id).filter_by(user_id=user_id).all()
        elif int(type) == 1:
            beaches_id = db.session.query(Comments.beach_id).filter_by(user_id=user_id).all()
        else:
            return {"Error":"not supported option"}, 410

        ids = [row[0] for row in beaches_id]
        beaches = db.session.query(Beach).filter(Beach.id.in_(ids)).all()
        return jsonify([beach.convert_to_json() for beach in beaches]), 200

    except Exception as e:
        return {"Error": str(e)}


# Extra hello and docs
@routes_beaches.route('/api')
def api_runing():
    return jsonify("HELLO SURFER"), 200

@routes_beaches.route('/docs')
def docs():
    return render_template('docs.html')


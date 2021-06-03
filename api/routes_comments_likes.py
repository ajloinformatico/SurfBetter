from flask import Blueprint, jsonify, request
from flask_praetorian import auth_required
import flask_praetorian
from extensions import db
from models import Likes, Comments, LikesOfComment, Beach

routes_comments_likes = Blueprint('routes_comments_likes', __name__)


@routes_comments_likes.route("/api/beach/like", methods=['POST'])
@auth_required
def add_like_beach():
    """Add beach like"""
    req = request.get_json(force=True)
    beach_id = req["beach_id"]
    user_id = flask_praetorian.current_user_id()

    if db.session.query(Likes).filter_by(
            user_id=user_id,
            beach_id=beach_id
    ).count() > 0:
        return {"Error": "Comment already exists"}, 500

    try:
        db.session.add(
            Likes(
                user_id=user_id,
                beach_id=beach_id
            )
        )
        db.session.commit()
    except Exception as e:
        return {"Error", str(e)}, 500

    new_like_id = db.session.query(Likes.id).filter_by(user_id=user_id, beach_id=beach_id).first()
    return jsonify(f"Like with id {new_like_id} added correctly"), 200


@routes_comments_likes.route("/api/beach/like", methods=['DELETE'])
@auth_required
def delete_like_beach():
    """Delete a like on beach"""
    req = request.get_json(force=True)
    beach_id = req["beach_id"]
    user_id = flask_praetorian.current_user_id()
    try:
        db.session.query(Likes).filter_by(beach_id=beach_id, user_id=user_id).delete()
        db.session.commit()
    except Exception as e:
        return {"Error", str(e)}, 500
    return jsonify(f"Like with id {beach_id} deleted success"), 200


@routes_comments_likes.route("/api/beach/comment", methods=['POST'])
@auth_required
def add_comment():
    """ Send a commentary to one beach"""
    req = request.get_json(force=True)
    beach_id = req["beach_id"]
    comment = req["comment"]
    user_id = flask_praetorian.current_user_id()
    try:
        db.session.add(
            Comments(
                comment=comment,
                user_id=user_id,
                beach_id=beach_id
            )
        )
        db.session.commit()
    except Exception as e:
        return {"Error": str(e)}, 500
    comment_id = db.session.query(Comments.id).filter_by(user_id=user_id, beach_id=beach_id).first()
    return {"message": f"comment with id {comment_id} post correctly"}, 200
    # Test it if not run
    # return get_one_beach_info(beach_id), 200


@routes_comments_likes.route("/api/beach/comment/delete", methods=["DELETE"])
@auth_required
def delete_comment():
    """Delete a comment"""
    try:
        req = request.get_json(force=True)
        db.session.query(Comments).filter_by(id=req["comment_id"]).delete()
        db.session.commit()
        return {"message": f"comment with id {req['comment_id']} has been deleted"}, 200
    except Exception as e:
        return {"Error", str(e)}, 500


@routes_comments_likes.route("/api/beach/comment/like", methods=["POST"])
@auth_required
def add_like_comment():
    """Add like on a comment"""
    req = request.get_json(force=True)
    comment_id = req["comment_id"]
    user_id = flask_praetorian.current_user_id()

    if db.session.query(LikesOfComment).filter_by(
            user_id=user_id,
            comment_id=comment_id
    ).count() > 0:
        return jsonify("comment already exists"), 500

    try:
        db.session.add(
            LikesOfComment(
                user_id=user_id,
                comment_id=comment_id
            )
        )
        db.session.commit()
    except Exception as e:
        return {"Error", str(e)}, 500
    like_on_comment_id = db.session.query(LikesOfComment.id).filter_by(comment_id=comment_id, user_id=user_id).first()
    return {"message": f"Like with id {like_on_comment_id} added success"}, 200


@routes_comments_likes.route("/api/beach/comment/like", methods=["DELETE"])
@auth_required
def delete_like_comment():
    try:
        req = request.get_json(force=True)
        comment_id = req["comment_id"]
        user_id = flask_praetorian.current_user_id()
        try:
            db.session.query(LikesOfComment).filter_by(comment_id=comment_id, user_id=user_id).delete()
            db.session.commit()
        except:
            return {"Error": "Something was wrong with the delete"}, 500

        return {"message": f"Like with id {comment_id} deleted success"}, 200
    except Exception as e:
        return {"Error": str(e)}


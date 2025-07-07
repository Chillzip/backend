from flask import Blueprint

user_bp = Blueprint('user', __name__)

@user_bp.route("/test")
def test_user():
    return {"message": "User route is working!"}
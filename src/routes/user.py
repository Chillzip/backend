from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__)

@user_bp.route('/test', methods=['GET'])
def test_user():
    return jsonify({'message': 'User route is working!'})
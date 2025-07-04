from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from src.models.user import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()

        if not data:
            return jsonify({'message': 'No input data provided'}), 400

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({'message': 'Missing required fields'}), 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'message': 'User already exists'}), 409

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        print(f"✅ Registered user: {username} ({email})")
        return jsonify({'message': 'User registered successfully'}), 201

    except Exception as e:
        print(f"❌ Registration error: {e}")
        return jsonify({'message': 'Internal server error'}), 500

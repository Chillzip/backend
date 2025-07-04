from flask import Flask, send_from_directory
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import stripe

from src.models.user import db, User
from src.routes.user import user_bp
from src.routes.auth import auth_bp
from src.routes.payment import payment_bp
from src.routes.process import process_bp

app = Flask(__name__, static_folder="../frontend/dist/static", static_url_path="/static")

# Basic route to confirm backend is running
@app.route('/')
def index():
    return "Backend is running!"

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(payment_bp, url_prefix='/payment')
app.register_blueprint(process_bp, url_prefix='/process')

# Configurations
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chillzip.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "your-secret-key-here"  # Replace with your actual secret key

# Initialize extensions
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
CORS(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)

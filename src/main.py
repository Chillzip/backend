from flask import Flask
from routes.auth import auth_bp
from routes.user import user_bp
from routes.payment import payment_bp
from routes.process import process_bp

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(payment_bp, url_prefix='/payment')
    app.register_blueprint(process_bp, url_prefix='/process')

    return app

app = create_app()
from flask import Flask
from src.routes.test import test_bp
from src.routes.user import user_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(test_bp, url_prefix="/test")
app.register_blueprint(user_bp, url_prefix="/user")

if __name__ == "__main__":
    app.run(debug=True)
import os
from flask import Flask
from flask_cors import CORS
from app.extensions import db
from dotenv import load_dotenv

# Load local .env file if it exists
load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Load configuration from environment variables (Supabase URL & Secret Key)
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("No DATABASE_URL set for the application. Check your environment variables!")
        
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "fallback-secret-key")

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    from app.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


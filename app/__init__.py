import os
from flask import Flask
from dotenv import load_dotenv

# 1. Load the secrets from your hidden .env file into memory
load_dotenv()

def create_app():
    app = Flask(__name__)

    # 2. Pull the individual database credentials safely from the environment
    db_user = os.getenv("DATABASE_USER")
    db_password = os.getenv("DATABASE_PASSWORD")
    db_host = os.getenv("DATABASE_HOST")
    db_name = os.getenv("DATABASE_NAME")

    # 3. Dynamically build the secure connection URL
    database_uri = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"
    
    # 4. Apply configuration to your Flask app
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("JWT_SECRET", "default_fallback_secret_key")

    # Keep your existing blueprint registrations or routes below this line:
    # Example:
    # from app.routes import main_bp
    # app.register_blueprint(main_bp)

    return app


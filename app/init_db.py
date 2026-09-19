import os
from dotenv import load_dotenv

load_dotenv()

from app import create_app, db

app = create_app()

with app.app_context():
    print("Creating all database tables in Supabase...")
    db.create_all()
    print("Tables created successfully!")

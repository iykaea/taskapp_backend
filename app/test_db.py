import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATABASE_URL")

try:
    conn = psycopg2.connect(db_url)
    print("Successfully connected to Supabase PostgreSQL!")
    
    cur = conn.cursor()
    cur.execute("SELECT version();")
    record = cur.fetchone()
    print("Database version:", record)
    
    cur.close()
    conn.close()
    print("Connection closed.")
except Exception as e:
    print("Error connecting to the database:", e)

import os
from sqlalchemy import create_engine, text

db_url = 'postgresql://postgres.jwfstqyeixivdmtupuam:322Ik%C2%A3_-%23456%2F@aws-0-eu-west-1.pooler.supabase.com:6543/postgres?sslmode=require'
engine = create_engine(db_url)

with engine.connect() as conn:
    conn.execute(text('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(80) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    '''))
    conn.commit()
print('Table created successfully!')

import psycopg2

conn = psycopg2.connect(
    host="taskapp-db.cno46wmwi2lr.eu-north-1.rds.amazonaws.com",   
    database="postgres",
    user="taskappuser",
    password="432Ik566"
)
print("Connection successful!")
conn.close()

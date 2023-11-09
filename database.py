import psycopg2
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Replace these values with your database credentials
dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")

# Establish a connection to the PostgreSQL database
connection = psycopg2.connect(
    dbname=dbname, user=user, password=password, host=host, port=port
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Example: Execute a simple SQL query
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record)

cursor.execute("SELECT * FROM users;")
records = cursor.fetchall()
print(records)

# Don't forget to close the cursor and connection when done
cursor.close()
connection.close()

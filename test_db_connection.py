import mysql.connector
from mysql.connector import Error

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='flask_user',
        password='9090',
        database='career_counselor'
    )

try:
    connection = get_db_connection()
    if connection.is_connected():
        print("Successfully connected to the database.")
    else:
        print("Failed to connect to the database.")
except Error as e:
    print(f"Error: {e}")
finally:
    if connection and connection.is_connected():
        connection.close()



import sqlite3
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def get_db_connection():
    connection = sqlite3.connect('app/users.db')
    logging.info("Connection established with database.")
    return connection

def close_db_connection(connection):
    connection.close()
    logging.info("Connection closed with database.")

# Create the database and user table
def create_user_table():
    try:
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    hobby TEXT NOT NULL
                    )'''
            )
            logging.info("Table created or already exists.")
            connection.commit()
    except Exception as e:
        logging.error(f"Error creating table: {e}")

# Add a new user to the database
def add_user(name, age, hobby):
    try:
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                '''INSERT INTO users (name, age, hobby) VALUES (?, ?, ?)''', 
                (name, age, hobby)
            )
            logging.info("User added.")
            connection.commit()
    except Exception as e:
        logging.error(f"Error adding user: {e}")

# Update user information
def update_user(id, name, age, hobby):
    try:
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                '''UPDATE users
                   SET name = ?, age = ?, hobby = ?
                   WHERE id = ?''', 
                (name, age, hobby, id)
            )
            logging.info("User updated.")
            connection.commit()
    except Exception as e:
        logging.error(f"Error updating user: {e}")

# Delete a user from the database
def delete_user(id):
    try:
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                '''DELETE FROM users WHERE id = ?''', 
                (id,)
            )
            logging.info("User deleted.")
            connection.commit()
    except Exception as e:
        logging.error(f"Error deleting user: {e}")

# Get all users from the database
def get_users():
    try:
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM users''')
            user_list = cursor.fetchall()
            logging.info("Users fetched.")
            return user_list
    except Exception as e:
        logging.error(f"Error fetching users: {e}")
        return []

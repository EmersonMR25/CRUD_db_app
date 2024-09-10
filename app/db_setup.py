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

# Create the database
def create_user_table():
    connection = get_db_connection()
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
    close_db_connection(connection)

# Create a new user and add it to the database    
def add_user(name, age, hobby):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        '''INSERT INTO users (name, age, hobby) VALUES (?, ?, ?)''', 
        (name, age, hobby)
    )
    logging.info("User added.")
    connection.commit()
    close_db_connection(connection)

# Update info of a user
def update_user(id, name, age, hobby):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        '''UPDATE users
           SET name = ?, age = ?, hobby = ?
           WHERE id = ?''', 
        (name, age, hobby, id)
    )
    logging.info("User updated.")
    connection.commit()
    close_db_connection(connection)

# Delete a user
def delete_user(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        '''DELETE FROM users WHERE id = ?''', 
        (id,)
    )
    logging.info("User deleted.")
    connection.commit()
    close_db_connection(connection)

# Get all users from the db
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM users''')
    user_list = cursor.fetchall()
    logging.info("Users fetched.")
    close_db_connection(connection)
    return user_list

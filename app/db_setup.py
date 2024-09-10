import sqlite3

def create_user_table():
    try:
        with sqlite3.connect('app/users.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    hobby TEXT NOT NULL
                )
            ''')
            print("Table created successfully")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def add_user(name, age, hobby):
    try:
        with sqlite3.connect('app/users.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO user (name, age, hobby)
                VALUES (?, ?, ?, ?)
            ''', (name, age, hobby))
            connection.commit()
            print("User added successfully")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def get_users():
    try:
        with sqlite3.connect('app/users.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM user')
            users = cursor.fetchall()
            return users
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []


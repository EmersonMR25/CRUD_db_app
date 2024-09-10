import sqlite3

# Create the database
def create_user_table():
    # Create the connection with the db
    connection = sqlite3.connect('app/users.db')
    # Create a cursor object
    cursor = connection.cursor()
    # Execute the SQL command
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT NOT NULL
            )'''
    )
    # Commit the changes
    connection.commit()
    #Close the connection
    connection.close()
    
# Create a new user and add it to the database    
def add_user(name, age, hobby):
    # Create the connection with the db
    connection = sqlite3.connect('app/users.db')
    # Create a cursor object
    cursor = connection.cursor()
    # Execute the SQL command
    cursor.execute(
        # We use the ? placeholders in order to safeguard against SQL injections,
        # hence these are values that will be passed dynamically
        '''INSERT INTO user (name, age, hobby) VALUES (?, ?, ?)
        ''', (name, age, hobby)
    )
    # Commit the changes
    connection.commit()
    #Close the connection
    connection.close()
    
# Update info of an user
def update_user(id, name, age, hobby):
    # Create the connection with the db
    connection = sqlite3.connect('app/users.db')
    # Create a cursor object
    cursor = connection.cursor()
    # Execute the SQL command
    cursor.execute(
        '''UPDATE users
           SET name = ?, age = ?, hobby = ?
           WHERE id = ?
        ''', (id, name, age, hobby)
    )
    # Commit the changes
    connection.commit()
    # Close the connection
    connection.close()

# Delete an user
def delete_user(id):
    # Create the connection with the db
    connection = sqlite3.connect('app/users.db')
    # Create a cursor object
    cursor = connection.cursor()
    # Execute the SQL command
    cursor.execute(
        '''DELTE FROM users
           WHERE (id) VALUES (?)
        ''', (id)
    )
    # Commit the changes
    connection.commit()
    # Close the connection
    connection.close()
    

# Get all users from the db
def get_user():
    # Create the connection with the db
    connection = sqlite3.connect('app/users.db')
    # Create a cursor object
    cursor = connection.cursor()
    # Execute the SQL command
    cursor.execute(
        # We use the ? placeholders in order to safeguard against SQL injections,
        # hence these are values that will be passed dynamically
        '''SELECT *
           FROM users
        '''
    )
    # Get the fetched info
    user_list = cursor.fetchall()
    # Commit the changes
    connection.commit()
    # Close the connection
    connection.close()
    # Return the list
    return user_list



import sqlite3

# Create the database
def create_user_table():
    # Create the connection with the db
    connection = sqlite3.connect('app/users.db')
    print("Connection stablished with database,")
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
    print("Table created.")
    # Commit the changes
    connection.commit()
    #Close the connection
    connection.close()
    print("Connection closed with database,")
    
# Create a new user and add it to the database    
def add_user(name, age, hobby):
    # Create the connection with the db
    connection = sqlite3.connect('app/users.db')
    print("Connection stablished with database,")
    # Create a cursor object
    cursor = connection.cursor()
    # Execute the SQL command
    cursor.execute(
        # We use the ? placeholders in order to safeguard against SQL injections,
        # hence these are values that will be passed dynamically
        '''INSERT INTO user (name, age, hobby) VALUES (?, ?, ?)
        ''', (name, age, hobby)
    )
    print("User added.")
    # Commit the changes
    connection.commit()
    #Close the connection
    connection.close()
    print("Connection closed with database,")
    
    
# Update info of an user
def update_user(id, name, age, hobby):
    # Create the connection with the db
    connection = sqlite3.connect('app/users.db')
    print("Connection stablished with database,")
    # Create a cursor object
    cursor = connection.cursor()
    # Execute the SQL command
    cursor.execute(
        '''UPDATE users
           SET name = ?, age = ?, hobby = ?
           WHERE id = ?
        ''', (id, name, age, hobby)
    )
    print("User updated.")
    # Commit the changes
    connection.commit()
    # Close the connection
    connection.close()
    print("Connection closed with database,")

# Delete an user
def delete_user(id):
    # Create the connection with the db
    connection = sqlite3.connect('app/users.db')
    print("Connection stablished with database,")
    # Create a cursor object
    cursor = connection.cursor()
    # Execute the SQL command
    cursor.execute(
        '''DELTE FROM users
           WHERE (id) VALUES (?)
        ''', (id)
    )
    print("User updated.")
    # Commit the changes
    connection.commit()
    # Close the connection
    connection.close()
    print("Connection closed with database,")
    

# Get all users from the db
def get_user():
    # Create the connection with the db
    connection = sqlite3.connect('app/users.db')
    print("Connection stablished with database,")
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
    print("Users table fetched.")
    # Commit the changes
    connection.commit()
    # Close the connection
    connection.close()
    print("Connection closed with database,")
    # Return the list
    return user_list



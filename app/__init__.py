from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Ensure the database table is created
    #create_user_table()

    # Import and register routes
    from .routes import main_blueprint
    app.register_blueprint(main_blueprint)

    # Return the application
    return app

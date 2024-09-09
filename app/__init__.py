from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register routes
    from .routes import main_blueprint
    
    # Register the blueprint for the main routes in the application
    app.register_blueprint(main_blueprint)

    # Return the application
    return app
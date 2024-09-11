from app import create_app

# Create a Flask application instance
app = create_app()

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
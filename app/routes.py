from flask import Blueprint, render_template, request, redirect, url_for
from .db_setup import get_users, add_user, update_user, delete_user

# Create a blueprint for the main routes
main_blueprint = Blueprint('main', __name__)

# Render the main page
@main_blueprint.route("/")
def index():
    # Fetch all users from the database
    data = get_users()
    return render_template("index.html", data=data)

# Insert a new user into the database
@main_blueprint.route("/insert/", methods=['POST'])
def insert():
    if request.method == "POST":
        name = request.form.get("name")
        age = int(request.form.get("age"))
        hobby = request.form.get("hobby")
        
        # Add the user to the database
        add_user(name, age, hobby)
    
    return redirect(url_for("main.index"))

# Update user information
@main_blueprint.route("/update/<int:id>/", methods=['POST'])
def update(id):
    if request.method == "POST":
        name = request.form.get("name")
        age = int(request.form.get("age"))
        hobby = request.form.get("hobby")
        
        # Update the user's information in the database
        update_user(id, name, age, hobby)

    return redirect(url_for("main.index"))

# Delete a user from the database
@main_blueprint.route("/delete/<int:id>/", methods=['POST'])
def delete(id):
    if request.method == "POST":
        # Remove the user from the database
        delete_user(id)
    
    return redirect(url_for("main.index"))

from flask import Blueprint, render_template, request, redirect, url_for
from .db_setup import get_users, add_user, update_user, delete_user

# Create a blueprint for the main routes
main_blueprint = Blueprint('main', __name__)

# Create a connection and render the main page
@main_blueprint.route("/")
def index():
    # Fetch all users from the database
    data = get_users()
    return render_template("index.html", data=data)

@main_blueprint.route("/insert/", methods=['POST'])
def insert():
    # Insert the user into the database
    if request.method == "POST":
        name = request.form.get("name")
        age = int(request.form.get("age"))
        hobby = request.form.get("hobby")
        
        # Add the user to the database
        add_user(name, age, hobby)
    
    return redirect(url_for("main.index"))

@main_blueprint.route("/update/", methods=['POST'])
def update():
    # Update information of the user
    if request.method == "POST":
        id = int(request.form.get("id"))
        name = request.form.get("name")
        age = int(request.form.get("age"))
        hobby = request.form.get("hobby")
        
        # Update the user's information in the database
        update_user(id, name, age, hobby)

    return redirect(url_for("main.index"))

@main_blueprint.route("/delete/", methods=['POST'])
def delete():
    # Delete the user from the database
    if request.method == "POST":
        id = int(request.form.get("id"))
        
        # Remove the user from the database
        delete_user(id)
    
    return redirect(url_for("main.index"))

from flask import Blueprint, render_template, request, redirect, url_for
from .db_setup import add_user, get_users

# Create a blueprint for the main routes
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route("/")
def index():
    users = get_users()
    return render_template("index.html", users=users)

@main_blueprint.route("/add", methods=["POST"])
def add_user_route():
    name = request.form.get("name")
    age = request.form.get("age")
    hobby = request.form.get("hobby")
    
    if name and age and hobby:
        # Add user to the database
        add_user(name, age, hobby)
        return redirect(url_for('main.index'))
    else:
        # Handle invalid form data
        return "Invalid input. Please fill out all fields.", 400

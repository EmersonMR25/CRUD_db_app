from flask import Blueprint, render_template, request, redirect, url_for

# Create a blueprint for the main routes
main_blueprint = Blueprint('main', __name__)

# Create a connection and reder the main page
@main_blueprint.route("/")
def index():
    return render_template("index.html")

# Insert a new user into the database
@main_blueprint.route()
def ():
    return redirect(url_for("index"))

# Update information fron the database
@main_blueprint.route()
def ():
    return redirect(url_for("index"))

# Remove information from the database
@main_blueprint.route()
def ():
    return redirect(url_for("index"))

from flask import Blueprint, render_template, request, redirect, url_for
from .db_setup import add_user, get_users

# Create a blueprint for the main routes
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route("/")
def index():
    return render_template("index.html")


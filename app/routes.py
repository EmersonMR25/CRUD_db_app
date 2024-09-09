from flask import Blueprint, render_template

# Create a template
main_blueprint = Blueprint('main', __name__)

# Create the adress for the application
@main_blueprint.route("/")
def index():
    return render_template ("index.html")
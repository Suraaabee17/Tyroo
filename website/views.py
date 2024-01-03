from flask import Blueprint, render_template
# Blueprint means has a lot of urls

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html')

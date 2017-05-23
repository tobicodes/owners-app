from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
import os


app = Flask(__name__)
modus = Modus(app)

app.config['SQLALCHEMY_DATABASE_URI']='postgres://localhost/flask-blueprints'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

## We have a views.py file in project/owners/views that is our controller
## That file has the blueprint for our owners resource

## Let's get that blueprint and register it with our app that we just configured

from project.owners.views import owners_blueprint
from project.startups.views import startups_blueprint

app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(startups_blueprint, url_prefix='/owners/<int:id>/startups')

## Using the url_prefix means that we don't need to add 'owners' to each of our RESTful routes

@app.route('/')
def root():
	return "La pura vida"


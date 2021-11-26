from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# override base config settings and bind db instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# silence FSADeprecationWarning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from app.views import home
from app import config
from app.core.db import models
from app.core.db.models import * # pre-emptive imports


# this snippet must come AFTER the import block!
@app.before_first_request
def create_tables():
    db.create_all()

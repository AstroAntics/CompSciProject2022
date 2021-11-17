from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# override base config settings and bind db instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
db.create_all()

from app.views import home
from app import config
from app.core.db import models
from app.core.db.models import * # pre-emptive imports


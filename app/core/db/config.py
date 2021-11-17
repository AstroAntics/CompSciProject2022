from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app

# override base config settings and bind db instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

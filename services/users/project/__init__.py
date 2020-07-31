# services/users/project/__init__.py

import os
import sys
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


# instantiate the pap
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS') 
app.config.from_object(app_settings)

# instantiate db
db = SQLAlchemy(app)

# model
class User(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

# print(app.config, file=sys.stderr)

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
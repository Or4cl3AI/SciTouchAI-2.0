import os
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Importing modules from other files
from data_analysis import analyzeData
from machine_learning import MachineLearning
from ai_module import AIModule
from mobile_interface import MobileInterface
from responsive_design import ResponsiveDesign
from touchscreen_input import TouchscreenInput
from human_computer_interaction import HumanComputerInteraction
from natural_language_processing import NaturalLanguageProcessing
from software_engineering import SoftwareEngineering
from cyber_security import CyberSecurity
from encryption import encryptData
from authentication import authenticateUser
from aesthetics import Aesthetics
from usability import Usability
from journalism import Journalism
from music_theory import MusicTheory

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# User Class/Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password')

# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Create a User
@app.route('/user', methods=['POST'])
def add_user():
    username = request.json['username']
    password = request.json['password']

    new_user = User(username, password)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
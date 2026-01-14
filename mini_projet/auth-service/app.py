from flask import Flask, request, jsonify, send_from_directory
import jwt, datetime
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = "super_secret_key_microservices"

@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")

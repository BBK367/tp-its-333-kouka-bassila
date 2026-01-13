from app import app
from flask import render_template, request, jsonify

### EXO1 - simple API
@app.route('/api/salutation', methods=['GET'])
def salutation():
    return jsonify({"message": "Salut"})

### EXO2 - API with simple display
@app.route('/simple-html')
def simple_display():
    return "<h1>HTML simple </h1><p>Par El_Flaco27</p>"

### EXO3 - API with parameters display 
@app.route('/')
def index():
    user={'name':'javier','surname':'pastore'}
    return render_template('index.html',title='MDM',utilisateur=user)

### EXO4 - API with parameters retrieved from URL
@app.route('/user/<name>/<surname>')
def user(name,surname):
    user={'name':name,'surname':surname}
    return render_template('index.html',title='MDM',utilisateur=user)
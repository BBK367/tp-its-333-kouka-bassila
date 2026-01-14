from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
import datetime, jwt

app = Flask(__name__)

# =========================
# CONFIG
# =========================

SECRET_KEY = "ITS_SECRET_2026"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Swagger UI
Swagger(app)

# =========================
# MODELE
# =========================

class Etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    pin = db.Column(db.String(10), nullable=False)

# =========================
# JWT CHECK
# =========================

def check_token(token):
    if not token:
        return False
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except:
        return False

# =========================
# ROUTES HTML
# =========================

@app.route("/")
def home():
    return redirect("/login")

# ---------- LOGIN ----------
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    user = request.form["username"]
    pwd = request.form["password"]

    if user == "admin" and pwd == "admin":
        token = jwt.encode({
            "user": user,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, SECRET_KEY, algorithm="HS256")

        return render_template("token.html", token=token)

    return "Accès refusé"


# ---------- NEW STUDENT ----------
@app.route("/new", methods=["GET","POST"])
def new_student():
    token = request.args.get("token")

    if not check_token(token):
        return "⛔ Token invalide ou manquant"

    if request.method == "GET":
        return render_template("new.html", token=token)

    nom = request.form["nom"]
    addr = request.form["addr"]
    pin = request.form["pin"]

    e = Etudiant(nom=nom, addr=addr, pin=pin)
    db.session.add(e)
    db.session.commit()

    return redirect(f"/list?token={token}")


# ---------- LIST ----------
@app.route("/list")
def list_students():
    token = request.args.get("token")

    if not check_token(token):
        return "⛔ Token invalide ou manquant"

    rows = Etudiant.query.all()
    return render_template("list.html", rows=rows, token=token)


# =========================
# ROUTE API JSON + SWAGGER
# =========================

@app.route("/api/etudiants")
def api_etudiants():
    """
    Liste des étudiants
    ---
    responses:
      200:
        description: Liste de tous les étudiants
    """
    rows = Etudiant.query.all()
    return jsonify([
        {"id": e.id, "nom": e.nom, "addr": e.addr, "pin": e.pin}
        for e in rows
    ])


# =========================

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

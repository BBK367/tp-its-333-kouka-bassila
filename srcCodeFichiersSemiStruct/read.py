import json
import os
from flask import Flask, jsonify

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATIENT_FILE = os.path.join(BASE_DIR, "BDD102", "patient.json")

def charger_patients():
    with open(PATIENT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/api/patient/<int:id_patient>", methods=["GET"])
def get_patient_parametres(id_patient):
    patients = charger_patients()
    pid = str(id_patient)

    if pid not in patients:
        return jsonify({"erreur": "Patient non trouvé"}), 404

    return jsonify(patients[pid]["parametres"])

if __name__ == "__main__":
    app.run(debug=True)

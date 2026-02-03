from flask import Flask, request, jsonify

app = Flask(__name__)

patients = {}
counter = 1

@app.route("/api/patients", methods=["GET"])
def get_patients():
    return jsonify(list(patients.values()))

@app.route("/api/patients", methods=["POST"])
def add_patient():
    global counter
    data = request.json

    if not data.get("name") or not data.get("age"):
        return jsonify({"error": "Invalid data"}), 400

    patient = {
        "id": counter,
        "name": data["name"],
        "age": data["age"],
        "gender": data["gender"],
        "contact": data["contact"],
        "disease": data["disease"],
        "doctor": data["doctor"]
    }
    patients[counter] = patient
    counter += 1
    return jsonify(patient), 201

@app.route("/api/patients/<int:pid>", methods=["GET"])
def get_patient(pid):
    return jsonify(patients.get(pid, {}))

@app.route("/api/patients/<int:pid>", methods=["PUT"])
def update_patient(pid):
    if pid not in patients:
        return jsonify({"error": "Not found"}), 404

    patients[pid].update(request.json)
    return jsonify(patients[pid])

if __name__ == "__main__":
    app.run(debug=True)

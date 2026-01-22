from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data
users = [
    {"id": 1, "name": "Raja"},
    {"id": 2, "name": "Rama"}
]

# ---------------- HOME ----------------
@app.route("/", methods=["GET"])
def home():
    return "Welcome"

# ---------------- GET ALL USERS ----------------
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

# ---------------- GET SINGLE USER ----------------
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"message": "user not found"}), 404

# ---------------- CREATE USER ----------------
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    new_id = users[-1]["id"] + 1 if users else 1
    new_user = {"id": new_id, "name": data["name"]}
    users.append(new_user)
    return jsonify(new_user), 201

# ---------------- UPDATE USER (PUT) ----------------
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user["name"] = data["name"]
            return jsonify(user), 200
    return jsonify({"message": "user not found"}), 404

# ---------------- PARTIAL UPDATE (PATCH) ----------------
@app.route("/users/<int:user_id>", methods=["PATCH"])
def patch_user(user_id):     # ✅ UNIQUE FUNCTION NAME
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user.update(data)
            return jsonify(user), 200
    return jsonify({"message": "user not found"}), 404

# ---------------- DELETE USER ----------------
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"message": "user not found"}), 404

# ---------------- START SERVER ----------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

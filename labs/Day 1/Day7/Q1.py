from flask import Flask, jsonify, request

app = Flask(__name__)
users=[
    {"id": 1, "name": "beem"},
    {"id": 2, "name": "ram"},
]
#Base Url
@app.route("/")
def home():
    return "Question 1 – REST API Basics & Flask Server"

#Get All users
@app.route("/users",methods=['GET'])
def get_users():
    return jsonify(users),200
#Get Single User
@app.route("/users/<int:user_id>",methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error":"user not found"}),404
#Creating a user
@app.route("/users",methods=['POST'])
def post_user():
    data=request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400
    new_user = {"id":len(users)+1,
        "name": data.get("name"),}
    users.append(new_user)
    return jsonify(new_user),201
if __name__ == "__main__":
    app.run(debug=True)

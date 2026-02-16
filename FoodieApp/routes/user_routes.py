from flask import Blueprint, request
import uuid

user_bp = Blueprint("user", __name__, url_prefix="/api/v1")
users = {}

@user_bp.route("/users/register", methods=["POST"])
def register_user():
    data = request.json
    for u in users.values():
        if u["email"] == data["email"]:
            return {"error": "User exists"}, 409
    uid = str(uuid.uuid4())
    users[uid] = {"id": uid, **data}
    return users[uid], 201

from flask import Blueprint, request
import uuid

dish_bp = Blueprint("dish", __name__, url_prefix="/api/v1")

dishes = {}

# 🔵 Add Dish
@dish_bp.route("/restaurants/<rid>/dishes", methods=["POST"])
def add_dish(rid):
    data = request.json
    did = str(uuid.uuid4())
    dishes[did] = {
        "id": did,
        "restaurant_id": rid,
        "name": data["name"],
        "price": data["price"],
        "enabled": True
    }
    return dishes[did], 201


# 🔵 Update Dish
@dish_bp.route("/dishes/<did>", methods=["PUT"])
def update_dish(did):
    if did not in dishes:
        return {"error": "Not found"}, 404

    dishes[did].update(request.json)
    return dishes[did], 200


# 🔵 Enable / Disable Dish  ⭐ THIS WAS MISSING
@dish_bp.route("/dishes/<did>/status", methods=["PUT"])
def change_status(did):
    if did not in dishes:
        return {"error": "Not found"}, 404

    dishes[did]["enabled"] = request.json.get("enabled", True)
    return {"message": "Status updated"}, 200


# 🔵 Delete Dish
@dish_bp.route("/dishes/<did>", methods=["DELETE"])
def delete_dish(did):
    if did not in dishes:
        return {"error": "Not found"}, 404

    del dishes[did]
    return {"message": "Dish deleted"}, 200

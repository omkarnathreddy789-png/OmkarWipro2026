from flask import Blueprint, request
import uuid

restaurant_bp = Blueprint("restaurant", __name__, url_prefix="/api/v1")

restaurants = {}

@restaurant_bp.route("/restaurants", methods=["POST"])
def register_restaurant():

    data = request.get_json(force=True, silent=True)

    # prevent NoneType crash
    if not isinstance(data, dict):
        return {"error": "Invalid JSON"}, 400

    name = data.get("name")

    if not name:
        return {"error": "Name required"}, 400

    # duplicate check
    for r in restaurants.values():
        if r["name"] == name:
            return {"error": "Restaurant already exists"}, 409

    rid = str(uuid.uuid4())

    restaurants[rid] = {
        "id": rid,
        "name": name,
        "location": data.get("location"),
        "enabled": True
    }

    return restaurants[rid], 201


@restaurant_bp.route("/restaurants", methods=["GET"])
def get_all():
    return list(restaurants.values()), 200


@restaurant_bp.route("/restaurants/<rid>", methods=["GET"])
def view_restaurant(rid):
    if rid not in restaurants:
        return {"error": "Not found"}, 404
    return restaurants[rid], 200


@restaurant_bp.route("/restaurants/<rid>", methods=["PUT"])
def update_restaurant(rid):
    if rid not in restaurants:
        return {"error": "Not found"}, 404

    data = request.get_json(force=True, silent=True) or {}
    restaurants[rid].update(data)
    return restaurants[rid], 200


@restaurant_bp.route("/restaurants/<rid>/disable", methods=["PUT"])
def disable_restaurant(rid):
    if rid not in restaurants:
        return {"error": "Not found"}, 404

    restaurants[rid]["enabled"] = False
    return {"message": "Restaurant disabled"}, 200

@restaurant_bp.route("/restaurants/search", methods=["GET"])
def search_restaurants():

    name = request.args.get("name")
    location = request.args.get("location")
    dish = request.args.get("dish")
    rating = request.args.get("rating")

    result = []

    for r in restaurants.values():

        if name and name.lower() not in r["name"].lower():
            continue

        if location and r.get("location") != location:
            continue

        # dish & rating ignored for now (simple mock)
        result.append(r)

    return result, 200

from flask import Blueprint, request
import uuid

order_bp = Blueprint("order", __name__, url_prefix="/api/v1")

orders = {}

# -------------------------------------------------
# 🔵 Place Order (already used in user module)
# -------------------------------------------------
@order_bp.route("/orders", methods=["POST"])
def place_order():

    data = request.get_json(force=True)

    oid = str(uuid.uuid4())

    orders[oid] = {
        "id": oid,
        "user_id": data["user_id"],
        "restaurant_id": data["restaurant_id"],
        "dishes": data["dishes"]
    }

    return orders[oid], 201


# -------------------------------------------------
# 🟣 View Orders by Restaurant
# -------------------------------------------------
@order_bp.route("/restaurants/<rid>/orders", methods=["GET"])
def get_orders_by_restaurant(rid):

    result = [o for o in orders.values() if o["restaurant_id"] == rid]
    return result, 200


# -------------------------------------------------
# 🔴 View Orders by User
# -------------------------------------------------
@order_bp.route("/users/<uid>/orders", methods=["GET"])
def get_orders_by_user(uid):

    result = [o for o in orders.values() if o["user_id"] == uid]
    return result, 200

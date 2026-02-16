from flask import Blueprint

admin_bp = Blueprint("admin", __name__, url_prefix="/api/v1/admin")

@admin_bp.route("/restaurants/<rid>/approve", methods=["PUT"])
def approve_restaurant(rid):
    return {"message":"Restaurant approved"}, 200

@admin_bp.route("/restaurants/<rid>/disable", methods=["PUT"])
def disable_restaurant_admin(rid):
    return {"message":"Restaurant disabled"}, 200

@admin_bp.route("/feedback", methods=["GET"])
def view_feedback():
    return [], 200

@admin_bp.route("/orders", methods=["GET"])
def view_orders():
    return [], 200

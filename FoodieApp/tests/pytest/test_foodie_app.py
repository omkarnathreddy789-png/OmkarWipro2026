import requests
import uuid

BASE_URL = "http://127.0.0.1:5000/api/v1"


def test_full_foodie_app_flow():

    # ---------------------------------------------------
    # 1️⃣ RESTAURANT MODULE
    # ---------------------------------------------------
    rname = f"Rest_{uuid.uuid4().hex[:5]}"

    rest = requests.post(
        f"{BASE_URL}/restaurants",
        json={"name": rname, "location": "Vizag"}
    )
    assert rest.status_code == 201
    rid = rest.json()["id"]

    # view restaurant
    view = requests.get(f"{BASE_URL}/restaurants/{rid}")
    assert view.status_code == 200

    # ---------------------------------------------------
    # 2️⃣ DISH MODULE
    # ---------------------------------------------------
    dish = requests.post(
        f"{BASE_URL}/restaurants/{rid}/dishes",
        json={"name": "Biryani", "price": 250}
    )
    assert dish.status_code == 201
    did = dish.json()["id"]

    # update dish
    upd = requests.put(
        f"{BASE_URL}/dishes/{did}",
        json={"price": 300}
    )
    assert upd.status_code == 200

    # disable dish
    dis = requests.put(
        f"{BASE_URL}/dishes/{did}/status",
        json={"enabled": False}
    )
    assert dis.status_code == 200

    # ---------------------------------------------------
    # 3️⃣ ADMIN MODULE
    # ---------------------------------------------------
    approve = requests.put(
        f"{BASE_URL}/admin/restaurants/{rid}/approve"
    )
    assert approve.status_code == 200

    adm_disable = requests.put(
        f"{BASE_URL}/admin/restaurants/{rid}/disable"
    )
    assert adm_disable.status_code == 200

    feedback = requests.get(f"{BASE_URL}/admin/feedback")
    assert feedback.status_code == 200

    orders_admin = requests.get(f"{BASE_URL}/admin/orders")
    assert orders_admin.status_code == 200

    # ---------------------------------------------------
    # 4️⃣ USER MODULE
    # ---------------------------------------------------
    email = f"user{uuid.uuid4().hex[:4]}@test.com"

    user = requests.post(
        f"{BASE_URL}/users/register",
        json={"name": "TestUser", "email": email, "password": "1234"}
    )
    assert user.status_code == 201
    uid = user.json()["id"]

    # search restaurants
    search = requests.get(
        f"{BASE_URL}/restaurants/search?name=&location=&dish=&rating="
    )
    assert search.status_code == 200

    # ---------------------------------------------------
    # 5️⃣ ORDER MODULE
    # ---------------------------------------------------
    order = requests.post(
        f"{BASE_URL}/orders",
        json={"user_id": uid, "restaurant_id": rid, "dishes": [did]}
    )
    assert order.status_code == 201
    oid = order.json()["id"]

    # rating
    rating = requests.post(
        f"{BASE_URL}/ratings",
        json={"order_id": oid, "rating": 5, "comment": "Nice"}
    )
    assert rating.status_code == 201

    # view orders by restaurant
    view_rest_orders = requests.get(
        f"{BASE_URL}/restaurants/{rid}/orders"
    )
    assert view_rest_orders.status_code == 200

    # view orders by user
    view_user_orders = requests.get(
        f"{BASE_URL}/users/{uid}/orders"
    )
    assert view_user_orders.status_code == 200

    # ---------------------------------------------------
    # 🔴 DELETE DISH (CLEANUP)
    # ---------------------------------------------------
    delete = requests.delete(f"{BASE_URL}/dishes/{did}")
    assert delete.status_code == 200

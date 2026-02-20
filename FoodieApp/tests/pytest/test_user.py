import requests
import uuid

BASE_URL = "http://127.0.0.1:5000/api/v1"


def test_user_module():

    email = f"user{uuid.uuid4().hex[:4]}@test.com"

    # 1️⃣ Register user
    user = requests.post(
        f"{BASE_URL}/users/register",
        json={
            "name": "TestUser",
            "email": email,
            "password": "1234"
        }
    )
    assert user.status_code == 201
    uid = user.json()["id"]

    # 2️⃣ Create restaurant
    rest = requests.post(
        f"{BASE_URL}/restaurants",
        json={"name": "TestRest", "location": "Vizag"}
    )
    assert rest.status_code == 201
    rid = rest.json()["id"]

    # 3️⃣ Add dish
    dish = requests.post(
        f"{BASE_URL}/restaurants/{rid}/dishes",
        json={"name": "Biryani", "price": 200}
    )
    assert dish.status_code == 201
    did = dish.json()["id"]

    # 4️⃣ Place order
    order = requests.post(
        f"{BASE_URL}/orders",
        json={"user_id": uid, "restaurant_id": rid, "dishes": [did]}
    )
    assert order.status_code == 201
    oid = order.json()["id"]

    # 5️⃣ Rating
    rate = requests.post(
        f"{BASE_URL}/ratings",
        json={"order_id": oid, "rating": 5, "comment": "Nice"}
    )
    assert rate.status_code == 201

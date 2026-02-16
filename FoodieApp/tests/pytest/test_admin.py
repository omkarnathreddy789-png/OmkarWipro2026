import requests
import uuid

BASE_URL = "http://127.0.0.1:5000/api/v1"

def test_admin_routes():

    # 1️⃣ create restaurant
    rname = f"AdminRest_{uuid.uuid4().hex[:4]}"
    rest = requests.post(
        f"{BASE_URL}/restaurants",
        json={"name": rname, "location":"Vizag"}
    )
    assert rest.status_code == 201

    rid = rest.json()["id"]

    # 2️⃣ approve restaurant
    approve = requests.put(
        f"{BASE_URL}/admin/restaurants/{rid}/approve"
    )
    assert approve.status_code == 200

    # 3️⃣ disable restaurant
    disable = requests.put(
        f"{BASE_URL}/admin/restaurants/{rid}/disable"
    )
    assert disable.status_code == 200

    # 4️⃣ view feedback
    feedback = requests.get(
        f"{BASE_URL}/admin/feedback"
    )
    assert feedback.status_code == 200

    # 5️⃣ view orders
    orders = requests.get(
        f"{BASE_URL}/admin/orders"
    )
    assert orders.status_code == 200

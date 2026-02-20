import requests
import uuid

BASE_URL = "http://127.0.0.1:5000/api/v1"

def test_add_update_delete_dish():

    # 1️⃣ Create restaurant
    rname = f"Rest_{uuid.uuid4().hex[:4]}"
    rest = requests.post(
        f"{BASE_URL}/restaurants",
        json={"name": rname, "location": "Vizag"}
    )
    assert rest.status_code == 201

    rid = rest.json()["id"]

    # 2️⃣ Add dish
    dish = requests.post(
        f"{BASE_URL}/restaurants/{rid}/dishes",
        json={"name": "Paneer Curry", "price":180}
    )
    assert dish.status_code == 201

    did = dish.json()["id"]

    # 3️⃣ Update dish
    update = requests.put(
        f"{BASE_URL}/dishes/{did}",
        json={"price":200}
    )
    assert update.status_code == 200

    # 4️⃣ Disable dish
    disable = requests.put(
        f"{BASE_URL}/dishes/{did}/status",
        json={"enabled": False}
    )
    assert disable.status_code == 200

    # 5️⃣ Delete dish
    delete = requests.delete(
        f"{BASE_URL}/dishes/{did}"
    )
    assert delete.status_code == 200

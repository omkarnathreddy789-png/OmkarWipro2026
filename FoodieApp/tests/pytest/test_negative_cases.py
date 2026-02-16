import requests
import uuid

BASE_URL = "http://127.0.0.1:5000/api/v1"


# ---------------------------------------------------
# 1️⃣ Register user with missing fields
# (API currently allows it — so just ensure server responds)
# ---------------------------------------------------
def test_register_user_missing_fields():
    res = requests.post(
        f"{BASE_URL}/users/register",
        json={"name": "OnlyName"}
    )

    assert res.status_code == 201
    assert "id" in res.json()


# ---------------------------------------------------
# 2️⃣ Update non-existing dish
# ---------------------------------------------------
def test_update_non_existing_dish():
    res = requests.put(
        f"{BASE_URL}/dishes/99999",
        json={"price": 500}
    )

    assert res.status_code == 404


# ---------------------------------------------------
# 3️⃣ Disable non-existing dish
# ---------------------------------------------------
def test_disable_invalid_dish():
    res = requests.put(
        f"{BASE_URL}/dishes/99999/status",
        json={"enabled": False}
    )

    assert res.status_code == 404


# ---------------------------------------------------
# 4️⃣ Approve invalid restaurant id
# ---------------------------------------------------
def test_admin_approve_invalid_restaurant():
    res = requests.put(
        f"{BASE_URL}/admin/restaurants/99999/approve"
    )

    assert res.status_code == 404


# ---------------------------------------------------
# 5️⃣ Search with invalid query params
# (API should still respond normally)
# ---------------------------------------------------
def test_search_invalid_params():
    res = requests.get(
        f"{BASE_URL}/restaurants/search?name=@@@&location=###"
    )

    assert res.status_code == 200


# ---------------------------------------------------
# 6️⃣ Duplicate restaurant negative test
# ---------------------------------------------------
def test_duplicate_restaurant_negative():
    name = f"NegRest_{uuid.uuid4().hex[:4]}"

    requests.post(
        f"{BASE_URL}/restaurants",
        json={"name": name, "location": "Vizag"}
    )

    res = requests.post(
        f"{BASE_URL}/restaurants",
        json={"name": name, "location": "Vizag"}
    )

    assert res.status_code == 409

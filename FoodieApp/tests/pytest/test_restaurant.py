import requests
import uuid

BASE_URL = "http://127.0.0.1:5000/api/v1"

def test_add_restaurant():
    unique_name = f"FoodHub_{uuid.uuid4().hex[:6]}"

    res = requests.post(
        f"{BASE_URL}/restaurants",
        json={"name": unique_name, "location": "Hyderabad"}
    )

    assert res.status_code == 201
    assert res.json()["name"] == unique_name


def test_duplicate_restaurant():
    name = f"FoodHub_{uuid.uuid4().hex[:6]}"

    # First request → create restaurant
    requests.post(
        f"{BASE_URL}/restaurants",
        json={"name": name, "location": "Hyderabad"}
    )

    # Second request → duplicate
    res = requests.post(
        f"{BASE_URL}/restaurants",
        json={"name": name, "location": "Hyderabad"}
    )

    assert res.status_code == 409

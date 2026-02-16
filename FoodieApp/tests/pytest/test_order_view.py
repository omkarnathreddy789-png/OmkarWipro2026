import requests
import uuid

BASE_URL = "http://127.0.0.1:5000/api/v1"

def test_view_orders():

    # create user
    email = f"user{uuid.uuid4().hex[:4]}@test.com"
    user = requests.post(
        f"{BASE_URL}/users/register",
        json={"name":"Test","email":email,"password":"1234"}
    )
    uid = user.json()["id"]

    # create restaurant
    rest = requests.post(
        f"{BASE_URL}/restaurants",
        json={"name":f"Rest_{uuid.uuid4().hex[:4]}","location":"Vizag"}
    )
    rid = rest.json()["id"]

    # add dish
    dish = requests.post(
        f"{BASE_URL}/restaurants/{rid}/dishes",
        json={"name":"Pizza","price":300}
    )
    did = dish.json()["id"]

    # place order
    order = requests.post(
        f"{BASE_URL}/orders",
        json={"user_id":uid,"restaurant_id":rid,"dishes":[did]}
    )
    assert order.status_code == 201

    # view by restaurant
    by_rest = requests.get(
        f"{BASE_URL}/restaurants/{rid}/orders"
    )
    assert by_rest.status_code == 200

    # view by user
    by_user = requests.get(
        f"{BASE_URL}/users/{uid}/orders"
    )
    assert by_user.status_code == 200

import requests

BASE_URL = "http://127.0.0.1:5000"

def test_get_all_movies():
    response = requests.get(f"{BASE_URL}/api/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_movie_by_id():
    response = requests.get(f"{BASE_URL}/api/movies/101")
    assert response.status_code == 200
    assert response.json()["movie_name"] == "Interstellar"


def test_add_movie():
    payload = {
        "movie_name": "Avatar",
        "language": "English",
        "duration": "2h 42m",
        "price": 350
    }
    response = requests.post(f"{BASE_URL}/api/movies", json=payload)
    assert response.status_code == 201
    assert response.json()["movie_name"] == "Avatar"


def test_update_movie():
    payload = {
        "price": 400
    }
    response = requests.put(f"{BASE_URL}/api/movies/101", json=payload)
    assert response.status_code == 200
    assert response.json()["price"] == 400


def test_delete_movie_not_found():
    response = requests.delete(f"{BASE_URL}/api/movies/999")
    assert response.status_code == 404

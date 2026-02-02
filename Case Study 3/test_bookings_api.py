import requests

BASE_URL = "http://127.0.0.1:5000"

def test_book_ticket_success():
    payload = {
        "name": "John",
        "movie_id": 101,
        "tickets": 2
    }
    response = requests.post(f"{BASE_URL}/api/bookings", json=payload)
    assert response.status_code == 201
    assert response.json()["message"] == "Booking successful"


def test_booking_without_name():
    payload = {
        "movie_id": 101,
        "tickets": 2
    }
    response = requests.post(f"{BASE_URL}/api/bookings", json=payload)
    assert response.status_code == 400


def test_booking_invalid_ticket_count():
    payload = {
        "name": "Alex",
        "movie_id": 101,
        "tickets": 0
    }
    response = requests.post(f"{BASE_URL}/api/bookings", json=payload)
    assert response.status_code == 400

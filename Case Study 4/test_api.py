import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api/patients"

# ---------------- BASIC API TESTS ----------------
def test_create_patient():
    payload = {
        "name": "John",
        "age": 30,
        "gender": "Male",
        "contact": "9999999999",
        "disease": "Flu",
        "doctor": "Dr. Smith"
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "John"


def test_get_patients():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_negative_missing_name():
    response = requests.post(BASE_URL, json={"age": 25})
    assert response.status_code == 400


@pytest.mark.parametrize(
    "name, age, gender, disease",
    [
        ("Alice", 25, "Female", "Cold"),
        ("Mark", 40, "Male", "Fever")
    ]
)
def test_create_patient_parameterized(name, age, gender, disease):
    payload = {
        "name": name,
        "age": age,
        "gender": gender,
        "contact": "9999999999",
        "disease": disease,
        "doctor": "Dr. Smith"
    }

    # ✅ MISSING LINE (THIS FIXES THE ERROR)
    response = requests.post(BASE_URL, json=payload)

    assert response.status_code == 201
    assert response.json()["name"] == name


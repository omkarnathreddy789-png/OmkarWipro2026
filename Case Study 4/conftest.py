import pytest

@pytest.fixture
def patient_payload():
    return {
        "name": "Alice",
        "age": 28,
        "gender": "Female",
        "contact": "8888888888",
        "disease": "Cold",
        "doctor": "Dr. Adams"
    }

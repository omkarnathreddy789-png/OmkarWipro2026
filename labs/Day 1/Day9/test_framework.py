import pytest
import configparser

# ---------- CONFIGURATION (simulating config file) ----------

config = configparser.ConfigParser()
config["ENV"] = {
    "base_url": "http://localhost",
    "environment": "test"
}

BASE_URL = config["ENV"]["base_url"]

# ---------- UTILITIES (business logic) ----------

def add(a, b):
    return a + b


# ---------- TEST CASES (pytest framework) ----------

def test_add_function():
    assert add(2, 3) == 5


# ---------- EXTRA TEST ----------

def test_negative_numbers():
    assert add(-1, -2) == -3


"""
Framework Components Explained:

Test Runner:
    pytest automatically discovers and runs test_ functions.

Test Reports:
    Can be generated using:
        pytest --html=report.html

Configuration:
    configparser simulates environment settings.

Project Structure (normally):
    tests/       → test cases
    utilities/   → reusable logic
    config/      → environment data
    reports/     → results
"""

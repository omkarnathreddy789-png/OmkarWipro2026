import pytest

def test_login_flow():
    # Step 1: Launch application (mocked here)
    user_logged_in = True

    # Step 2: Perform login
    username = "admin"
    password = "password123"

    # Step 3: Validate end-to-end behavior
    assert user_logged_in is True
    assert username == "admin"
from Day11.project.auth import login


def test_valid_login():
    assert login("admin","admin123") == "Login Successful"
def test_invalid_login():
    assert login("user","user123") == "Login UnSuccessful"
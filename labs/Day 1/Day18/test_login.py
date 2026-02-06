from pages.login_page import LoginPage
from config.config import BASE_URL, USERNAME, PASSWORD

def test_valid_login(driver):
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.login(USERNAME, PASSWORD)

    msg = login.get_message()
    print("\nLogin Message:", msg)

    assert "You logged into a secure area!" in msg

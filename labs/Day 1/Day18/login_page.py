from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class LoginPage(BasePage):

    username = (By.ID, "username")
    password = (By.ID, "password")
    login_btn = (By.CSS_SELECTOR, "button[type='submit']")
    message = (By.ID, "flash")

    def open(self, url):
        self.driver.get(url)

    def login(self, user, pwd):
        self.type(self.username, user)
        self.type(self.password, pwd)
        self.click(self.login_btn)

    def get_message(self):
        return self.get_text(self.message)

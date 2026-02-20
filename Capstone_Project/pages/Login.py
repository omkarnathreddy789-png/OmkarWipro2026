from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ----------- LOCATORS ------------

    login_btn = (By.LINK_TEXT, "My Account")



    email_input= (By.XPATH, "//input[@id='username']")
    password_input = (By.XPATH, "//input[@id='password']")

    login = (By.XPATH, "//input[@name='login']")
    checkbox=(By.ID,"rememberme")
    greeting_message = (By.CSS_SELECTOR, "p strong")
    sign_out_link = (By.LINK_TEXT, "Sign out")
    # ----------- METHODS ------------

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()
    def enter_email(self, value):
        self.wait.until(
            EC.element_to_be_clickable(self.email_input)
        ).send_keys(value)

    def enter_password(self,name):
        self.wait.until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(name)


    def click_loginbtn(self):
        self.wait.until(EC.element_to_be_clickable(self.login)).click()

    def click_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(self.checkbox)).click()

    def get_logged_in_username(self):
        """Return the username displayed after login"""
        element = self.wait.until(EC.visibility_of_element_located(self.greeting_message))
        return element.text

    def assert_login_success(self, expected_username):
        """Assert that the login was successful by checking the username"""
        actual_username = self.get_logged_in_username()
        assert actual_username == expected_username, f"Expected username '{expected_username}', but got '{actual_username}'"

    def sign_out(self):
        """Click the sign out link"""
        self.wait.until(EC.element_to_be_clickable(self.sign_out_link)).click()


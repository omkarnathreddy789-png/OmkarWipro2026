from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ----------- LOCATORS ------------

    sign_up_btn = (By.LINK_TEXT, "My Account")



    email_input= (By.ID, "reg_email")
    password_input =  (By.ID, "reg_password")
    password_strength = (By.CSS_SELECTOR, ".woocommerce-password-strength")

    register = (By.NAME, "register")
    logout_link = (By.LINK_TEXT, "Sign out")


    # ----------- METHODS ------------

    def click_sign_up(self):
        self.wait.until(EC.element_to_be_clickable(self.sign_up_btn)).click()

    def enter_email(self, value):
        self.wait.until(
            EC.element_to_be_clickable(self.email_input)
        ).send_keys(value)

    def enter_password(self, password):
        password_element = self.wait.until(
            EC.visibility_of_element_located(self.password_input)
        )

        password_element.clear()
        password_element.send_keys(password)

        # Wait until register button becomes enabled
        self.wait.until(
            lambda driver: driver.find_element(*self.register).is_enabled()
        )

    def click_register(self):
        register_button = self.wait.until(
            EC.element_to_be_clickable(self.register)
        )
        register_button.click()

    def is_registration_page_loaded(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.email_input)
        ).is_displayed()

    def is_registration_successful(self):

        try:
            self.wait.until(
                EC.visibility_of_element_located(self.logout_link)
            )
            return True

        except TimeoutException:
            return False

    def get_registration_error(self):
        elements = self.driver.find_elements(*self.error_message)
        if elements:
            return elements[0].text
        return None

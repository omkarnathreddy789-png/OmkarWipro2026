from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Capstone_Project.conftest import logger


class OrderProduct:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ----------- LOCATORS ------------
    click_shop = (By.XPATH, "//a[text()='Shop']")
    add_basket_btn = (By.XPATH, "//a[text()='Add to basket']")
    view_basket = (By.XPATH, "//a[text()='View Basket']")

    proceed_checkout= (By.XPATH, "//a[contains(@class,'checkout-button')]")
    firstName_input=(By.XPATH, "//input[@id='billing_first_name']")
    lastName_input=(By.XPATH, "//input[@id='billing_last_name']")
    companyName_input=(By.XPATH, "//input[@id='billing_company']")
    email_input=(By.XPATH, "//input[@id='billing_email']")
    phoneNumber_input=(By.XPATH, "//input[@id='billing_phone']")
    country_container = (By.ID, "s2id_billing_country")
    country_search_input = (By.XPATH, "//input[contains(@class,'select2-input')]")
    order_notes_input = (By.ID, "order_comments")
    country_result = (By.XPATH, "//div[@class='select2-result-label']")
    country_input = (By.ID, "billing_country")
    address_input = (By.XPATH, "//input[@id='billing_address_1']")
    city_input = (By.XPATH, "//input[@id='billing_city']")
    state_dropdown_container = (By.ID, "s2id_billing_state")
    state_results_list = (By.XPATH, "//ul[contains(@class,'select2-results')]")
    zipcode_input=(By.XPATH,"//input[@id='billing_postcode']")
    payment_method_radio = (By.ID, "payment_method_{}")
    place_order_btn = (By.ID, "place_order")
    success_msg = (By.CSS_SELECTOR, ".woocommerce-thankyou-order-received")

    # ----------- METHODS ------------

    def go_to_shop(self):
        self.wait.until(EC.element_to_be_clickable(self.click_shop)).click()

    def add_product_to_basket(self):
        """
        Uses Scroll + JavaScript click to avoid
        ElementClickInterceptedException caused by ads iframe
        """

        element = self.wait.until(
            EC.presence_of_element_located(self.add_basket_btn)
        )

        # Scroll element to center of screen
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

        # Ensure element is visible
        self.wait.until(EC.visibility_of(element))

        # JavaScript click (bypasses overlay issues)
        self.driver.execute_script("arguments[0].click();", element)



    def click_view_basket(self):
        self.wait.until(EC.element_to_be_clickable(self.view_basket)).click()

    def get_current_url(self):
        return self.driver.current_url

    def click_proceed_to_checkout(self):
        # self.wait.until(EC.element_to_be_clickable(self.proceed_checkout)).click()
        # Wait until button is present
        element = self.wait.until(EC.presence_of_element_located(self.proceed_checkout))

        # Scroll button into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Click using JavaScript to avoid overlay issues
        self.driver.execute_script("arguments[0].click();", element)

    def enter_first_name(self, first_name):
        field = self.wait.until(EC.visibility_of_element_located(self.firstName_input))
        field.clear()
        field.send_keys(first_name)

    def enter_last_name(self, last_name):
        field = self.wait.until(EC.visibility_of_element_located(self.lastName_input))
        field.clear()
        field.send_keys(last_name)

    def enter_company_name(self, company):
        field = self.wait.until(EC.visibility_of_element_located(self.companyName_input))
        field.clear()
        field.send_keys(company)

    def enter_email(self, email):
        field = self.wait.until(EC.visibility_of_element_located(self.email_input))
        field.clear()
        field.send_keys(email)

    def enter_phone(self, phone):
        field = self.wait.until(EC.visibility_of_element_located(self.phoneNumber_input))
        field.clear()
        field.send_keys(phone)

    def enter_order_notes(self, notes):
        field = self.wait.until(
            EC.visibility_of_element_located(self.order_notes_input)
        )
        field.clear()
        field.send_keys(notes)

    def select_country_using_search(self, country_code):
        """
        Selects the country by its code (e.g., 'IN' for India)
        Uses JS to set value because WooCommerce select2 dropdown can block clicks
        """
        self.driver.execute_script("""
            var select = document.getElementById('billing_country');
            select.value = arguments[0];
            select.dispatchEvent(new Event('change'));
        """, country_code)

    def enter_address(self, address):
        field = self.wait.until(EC.visibility_of_element_located(self.address_input) )
        field.clear()
        field.send_keys(address)

    def enter_city(self, city):
        field = self.wait.until(EC.visibility_of_element_located(self.city_input))
        field.clear()
        field.send_keys(city)

    def select_state(self, state_name):
        self.wait.until(
            EC.element_to_be_clickable(self.state_dropdown_container)
        ).click()
        state_option = (
            By.XPATH,
            f"//div[contains(@class,'select2-result-label') and normalize-space()='{state_name}']"
        )
        element = self.wait.until(EC.visibility_of_element_located(state_option))
        element.click()
        # Wait for the mask to disappear
        self.wait.until(EC.invisibility_of_element_located((By.ID, "select2-drop-mask")))

    def enter_zipcode(self, zipcode):
        field = self.wait.until(EC.visibility_of_element_located(self.zipcode_input))
        field.clear()
        field.send_keys(zipcode)

    def select_payment_method(self, value):
        # Create locator using static template
        dynamic_locator = (
            self.payment_method_radio[0],
            self.payment_method_radio[1].format(value)
        )

        radio = self.wait.until(
            EC.element_to_be_clickable(dynamic_locator)
        )

        # JS click (recommended for WooCommerce checkout)
        self.driver.execute_script("arguments[0].click();", radio)

    def click_place_order(self):
        # Wait for mask to disappear
        self.wait.until(EC.invisibility_of_element_located((By.ID, "select2-drop-mask")))
        # Click with JS to avoid interception
        element = self.wait.until(EC.element_to_be_clickable(self.place_order_btn))
        self.driver.execute_script("arguments[0].click();", element)

        # Wait until URL changes to order-received
        self.wait.until(lambda d: "order-received" in d.current_url)

    def get_success_message(self):
        logger.info("Waiting for success message")
        element = self.wait.until(
            EC.visibility_of_element_located(self.success_msg)
        )
        return element.text

    # order.select_payment_method("cod")
    # order.select_payment_method("bacs")
    # order.select_payment_method("cheque")
    # order.select_payment_method("ppec_paypal")
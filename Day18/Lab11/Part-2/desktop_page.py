from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class DesktopPage:
    """
    Page Factory style:
    All elements declared once and used everywhere
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ====== ELEMENT FACTORY ======

    desktops_tab = (By.LINK_TEXT, "Desktops")
    mac_link = (By.XPATH, "//a[text()='Mac']")
    sort_dropdown = (By.ID, "input-sort")
    add_to_cart_btn = (By.XPATH, "//button[contains(@onclick,'cart.add')]")

    search_box = (By.NAME, "search")
    search_button = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
    description_checkbox = (By.NAME, "description")

    mac_heading = (By.XPATH, "//h2[text()='Mac']")

    # ====== FACTORY METHODS ======

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def select_dropdown(self, locator, text):
        dropdown = Select(self.wait.until(EC.element_to_be_clickable(locator)))
        dropdown.select_by_visible_text(text)

    # ====== BUSINESS FLOWS ======

    def open_mac_page(self):
        self.click(self.desktops_tab)
        self.click(self.mac_link)

    def verify_mac_heading(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.mac_heading)
        ).is_displayed()

    def sort_name_az(self):
        self.select_dropdown(self.sort_dropdown, "Name (A - Z)")

    def add_to_cart(self):
        self.click(self.add_to_cart_btn)

    def search_product(self, value):
        self.type(self.search_box, value)
        self.click(self.search_button)

    def search_with_description(self):
        self.click(self.description_checkbox)
        self.click(self.search_button)

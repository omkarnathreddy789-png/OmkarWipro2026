from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class DesktopPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ========== LOCATORS ==========

    desktops_tab = (By.LINK_TEXT, "Desktops")

    mac_link = (By.XPATH, "//a[text()='Mac']")

    sort_dropdown = (By.ID, "input-sort")

    add_to_cart = (By.XPATH, "//button[contains(@onclick,'cart.add')]")

    search_box = (By.NAME, "search")

    search_button = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")

    description_checkbox = (By.NAME, "description")

    mac_heading = (By.XPATH, "//h2[text()='Mac']")

    # ========== ACTION METHODS ==========

    def go_to_mac(self):
        # Click Desktops menu first (not hover)
        desktops = self.wait.until(
            EC.element_to_be_clickable(self.desktops_tab)
        )
        desktops.click()

        # Now click Mac (appears after menu opens)
        mac = self.wait.until(
            EC.element_to_be_clickable(self.mac_link)
        )
        mac.click()

    def verify_mac_heading(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.mac_heading)
        ).is_displayed()

    def sort_name_az(self):
        dropdown = Select(
            self.wait.until(EC.element_to_be_clickable(self.sort_dropdown))
        )
        dropdown.select_by_visible_text("Name (A - Z)")

    def add_product_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.add_to_cart)
        ).click()

    def search_product(self, value):
        box = self.wait.until(
            EC.visibility_of_element_located(self.search_box)
        )
        box.clear()
        box.send_keys(value)
        self.wait.until(
            EC.element_to_be_clickable(self.search_button)
        ).click()

    def search_with_description(self):
        self.wait.until(
            EC.element_to_be_clickable(self.description_checkbox)
        ).click()
        self.wait.until(
            EC.element_to_be_clickable(self.search_button)
        ).click()

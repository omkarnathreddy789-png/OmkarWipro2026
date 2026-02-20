from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FilterProduct:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ----------- LOCATORS ------------
    click_shop = (By.XPATH, "//a[text()='Shop']")
    min_price_input = (By.XPATH, "//span[contains(@class,'ui-slider-handle')][1]")
    max_price_input =  (By.XPATH, "//span[contains(@class,'ui-slider-handle')][2]")
    filter_button = (By.XPATH, "//button[text()='Filter']")
    products=(By.CSS_SELECTOR, "ul.products li")

    # ----------- METHODS ------------
    def go_to_shop(self):
        self.wait.until(EC.element_to_be_clickable(self.click_shop)).click()
    def filter_by_price(self, min_price, max_price):
        # Set min price
        self.driver.execute_script(
            f"document.getElementById('min_price').value = '{min_price}';"
        )
        # Set max price
        self.driver.execute_script(
            f"document.getElementById('max_price').value = '{max_price}';"
        )

        # Click filter button
        self.wait.until(EC.element_to_be_clickable(self.filter_button)).click()


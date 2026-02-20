from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchProduct:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    #------LOCATORS-------
    click_shop = (By.XPATH, "//a[text()='Shop']")
    search_box = (By.ID, "s")
    search_result_link = (By.CSS_SELECTOR, "h2.post-title.entry-title a")
    search_box_value=(By.CSS_SELECTOR, "input[name='s']")
    product_title=(By.CSS_SELECTOR, "h1.product_title")
    #---------METHODS-------
    def go_to_shop(self):
        self.wait.until(EC.element_to_be_clickable(self.click_shop)).click()
    def search_product(self, product_name):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_box)
        )
        search_box.clear()
        search_box.send_keys(product_name + Keys.ENTER)


    def validate_search_results(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_result_link)
        )
        return True


    def click_search_result(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_result_link)
        ).click()
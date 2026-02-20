from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RemoveProduct:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ----------- LOCATORS ------------
    click_shop = (By.XPATH, "//a[text()='Shop']")
    add_basket_btn = (By.XPATH, "//a[text()='Add to basket']")
    view_basket = (By.XPATH, "//a[text()='View Basket']")
    remove_btn = (By.CSS_SELECTOR, "a.remove")

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

    def remove_product_from_cart(self, product_id=None):
        """
        Removes a product from the cart.
        If product_id is None, removes the first item in the cart.
        """
        if product_id:
            locator = (By.CSS_SELECTOR, f"a.remove[data-product_id='{product_id}']")
        else:
            locator = self.remove_btn

        remove_element = self.wait.until(EC.element_to_be_clickable(locator))
        remove_element.click()

        # Wait until the element disappears (cart refresh)
        self.wait.until(EC.staleness_of(remove_element))

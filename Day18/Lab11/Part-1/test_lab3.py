from selenium import webdriver
from pages.desktop_page import DesktopPage
import time

def test_lab3_flow():

    driver = webdriver.Firefox()
    driver.get("https://tutorialsninja.com/demo/")
    driver.implicitly_wait(10)

    page = DesktopPage(driver)

    page.go_to_mac()
    page.sort_name_az()
    page.add_product_to_cart()

    time.sleep(3)
    driver.quit()

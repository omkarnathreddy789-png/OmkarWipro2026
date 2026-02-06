from selenium import webdriver
from pages.desktop_page import DesktopPage
import time

def test_lab4_flow():

    driver = webdriver.Firefox()
    driver.get("https://tutorialsninja.com/demo/")
    driver.implicitly_wait(10)

    assert "Your Store" in driver.title

    page = DesktopPage(driver)

    page.go_to_mac()
    assert page.verify_mac_heading()

    page.sort_name_az()
    page.add_product_to_cart()

    page.search_product("Mobile")
    time.sleep(2)

    page.search_product("Monitors")
    page.search_with_description()

    time.sleep(3)
    driver.quit()

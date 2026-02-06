from selenium import webdriver
from pages.desktop_page import DesktopPage

def test_lab4_flow():

    driver = webdriver.Firefox()
    driver.get("https://tutorialsninja.com/demo/")
    driver.implicitly_wait(10)

    assert "Your Store" in driver.title

    page = DesktopPage(driver)

    page.open_mac_page()
    assert page.verify_mac_heading()

    page.sort_name_az()
    page.add_to_cart()

    page.search_product("Mobile")
    page.search_product("Monitors")
    page.search_with_description()

    driver.quit()

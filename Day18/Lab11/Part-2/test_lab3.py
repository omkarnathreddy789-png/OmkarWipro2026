from selenium import webdriver
from pages.desktop_page import DesktopPage

def test_lab3_flow():

    driver = webdriver.Firefox()
    driver.get("https://tutorialsninja.com/demo/")
    driver.implicitly_wait(10)

    page = DesktopPage(driver)

    page.open_mac_page()
    page.sort_name_az()
    page.add_to_cart()

    driver.quit()

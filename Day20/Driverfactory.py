from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

GRID_URL = "http://localhost:4444"

def get_driver(browser):
    print("Inside get_driver function")

    if browser.lower() == "chrome":
        options = ChromeOptions()
    elif browser.lower() == "firefox":
        options = FirefoxOptions()
    else:
        raise ValueError("Browser not supported")

    print("Connecting to Selenium Grid at", GRID_URL)

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    driver.maximize_window()
    return driver

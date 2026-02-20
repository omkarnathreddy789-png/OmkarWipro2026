from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import configparser
import os
def get_driver():

    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "../config/config.ini"))

    browser = config["DEFAULT"]["browser"].lower()

    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-autofill")
        chrome_options.add_argument("--disable-password-manager-reauthentication")
        chrome_options.add_argument("--disable-save-password-bubble")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        # -------- Firefox --------
    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--disable-notifications")
        firefox_options.add_argument("--disable-popup-blocking")
        firefox_options.add_argument("--disable-extensions")
        firefox_options.add_argument("--start-maximized")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options
        )

    else:
        raise Exception("Browser not supported")

    driver.implicitly_wait(int(config["DEFAULT"]["implicit_wait"]))

    return driver

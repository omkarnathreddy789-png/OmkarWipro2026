from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

TEST_URL = "https://www.google.com"
EXPECTED_TITLE = "Google"
GRID_URL = "http://localhost:4444"

browsers = ["chrome", "firefox"]

for browser in browsers:
    driver = None
    try:
        if browser == "chrome":
            options = ChromeOptions()
        else:
            options = FirefoxOptions()

        # TRY GRID FIRST
        try:
            driver = webdriver.Remote(
                command_executor=GRID_URL,
                options=options
            )
            execution = "GRID"
        except Exception:
            # FALLBACK TO LOCAL
            if browser == "chrome":
                driver = webdriver.Chrome(options=options)
            else:
                driver = webdriver.Firefox(options=options)
            execution = "LOCAL"

        driver.get(TEST_URL)

        assert EXPECTED_TITLE in driver.title

        caps = driver.capabilities
        print("================================")
        print("Execution :", execution)
        print("Browser   :", caps.get("browserName"))
        print("Platform  :", caps.get("platformName"))
        print("Title OK  :", driver.title)
        print("================================")

    except Exception as e:
        print("Test Failed:", e)

    finally:
        if driver:
            driver.quit()

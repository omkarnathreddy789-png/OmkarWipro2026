from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# 1. Launch browser
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# -------------------------------------------------
# 1. IMPLICIT WAIT (applies to all find_element calls)
# -------------------------------------------------
driver.implicitly_wait(10)  # seconds

# Locate the Enable button
enable_button = driver.find_element(By.XPATH, "//button[text()='Enable']")
enable_button.click()

# -------------------------------------------------
# 2. EXPLICIT WAIT (wait until input box is clickable)
# -------------------------------------------------
try:
    explicit_wait = WebDriverWait(driver, 15)
    input_box = explicit_wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
    )
    print("Explicit Wait: Input box is clickable")
except TimeoutException:
    print("Explicit Wait: Element not clickable in time")

# -------------------------------------------------
# 3. FLUENT WAIT (custom polling interval)
# -------------------------------------------------
try:
    fluent_wait = WebDriverWait(
        driver,
        timeout=15,
        poll_frequency=2,   # polling every 2 seconds
        ignored_exceptions=[Exception]
    )

    input_box_fluent = fluent_wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
    )

    print("Fluent Wait: Input box is available for interaction")
    input_box_fluent.send_keys("Selenium Waits Demo")

except TimeoutException:
    print("Fluent Wait: Element not available")

time.sleep(3)
driver.quit()

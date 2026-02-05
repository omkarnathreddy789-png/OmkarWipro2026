from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://letcode.in/window")
driver.maximize_window()

time.sleep(2)

# Click button that opens multiple windows
driver.find_element(By.ID, "multi").click()

time.sleep(2)

# Get all window handles
windows = driver.window_handles

# Switch to each window and print URL
for child in windows:
    driver.switch_to.window(child)
    print("Current URL:", driver.current_url)
    time.sleep(2)

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://letcode.in/alert")
driver.maximize_window()

time.sleep(2)

# Click Prompt Alert button
driver.find_element(By.ID, "prompt").click()

# Switch to alert
alert = driver.switch_to.alert

# Print alert message
print("Prompt alert text:", alert.text)

# Send text to prompt
alert.send_keys("Selenium Test")

time.sleep(1)

# Click OK
alert.accept()

time.sleep(2)
driver.quit()

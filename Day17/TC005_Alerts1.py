from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://letcode.in/alert")
driver.maximize_window()

time.sleep(2)

# Click Confirm Alert button
driver.find_element(By.ID, "confirm").click()

# Switch to alert
alert = driver.switch_to.alert

# Print alert message
print("Confirm alert text:", alert.text)

time.sleep(1)

# Click OK (use alert.dismiss() for Cancel)
alert.accept()

time.sleep(2)
driver.quit()

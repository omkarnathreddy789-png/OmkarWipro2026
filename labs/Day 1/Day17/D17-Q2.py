from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://letcode.in/alert")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Simple Alert
driver.find_element(By.ID, "accept").click()
alert = wait.until(EC.alert_is_present())
print("Simple Alert Text:", alert.text)
alert.accept()

# Confirm Alert
driver.find_element(By.ID, "confirm").click()
confirm_alert = wait.until(EC.alert_is_present())
print("Confirm Alert Text:", confirm_alert.text)
confirm_alert.dismiss()

# Prompt Alert
driver.find_element(By.ID, "prompt").click()
prompt_alert = wait.until(EC.alert_is_present())
print("Prompt Alert Text:", prompt_alert.text)
prompt_alert.send_keys("Selenium User")
prompt_alert.accept()

# Verify result
result = wait.until(EC.visibility_of_element_located((By.ID, "myName"))).text
print("Result on page:", result)

assert "Selenium User" in result

driver.quit()

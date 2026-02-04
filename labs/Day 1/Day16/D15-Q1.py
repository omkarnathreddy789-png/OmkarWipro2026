from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/text-box")
time.sleep(2)

# By ID
driver.find_element(By.ID, "userName").send_keys("Omkar Reddy")

# FIXED: Email field
driver.find_element(By.ID, "userEmail").send_keys("omkar@test.com")

# By CSS Selector
driver.find_element(By.CSS_SELECTOR, "textarea#currentAddress").send_keys("Hyderabad")

# By XPath
driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("Telangana")

# By Class Name
driver.find_element(By.CLASS_NAME, "btn-primary").click()

time.sleep(2)

output = driver.find_element(By.ID, "output").text

if "Omkar Reddy" in output:
    print("TEST PASSED – Form submitted successfully")
else:
    print("TEST FAILED")

time.sleep(3)
driver.quit()

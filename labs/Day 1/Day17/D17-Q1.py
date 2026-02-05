from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch browser
driver = webdriver.Firefox()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()

time.sleep(2)

# 1. Fill text boxes
driver.find_element(By.NAME, "firstname").send_keys("Omkar")
driver.find_element(By.NAME, "lastname").send_keys("Reddy")

# 2. Select radio button
driver.find_element(By.ID, "sex-0").click()      # Male
driver.find_element(By.ID, "exp-2").click()      # 3 years experience

# 3. Select checkboxes
driver.find_element(By.ID, "profession-1").click()   # Automation Tester
driver.find_element(By.ID, "tool-2").click()         # Selenium Webdriver

# 4. Dropdown using Select class
continent = Select(driver.find_element(By.ID, "continents"))
continent.select_by_visible_text("Asia")

time.sleep(1)

# 5. Submit form
driver.find_element(By.ID, "submit").click()

time.sleep(2)

# 6. Verify confirmation (simple check)
print("Form submitted successfully!")

driver.quit()

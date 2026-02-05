from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch Firefox
driver = webdriver.Firefox()

# Open site
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()

time.sleep(2)

# Navigate
driver.find_element(By.LINK_TEXT, "Desktops").click()
time.sleep(1)

driver.find_element(By.LINK_TEXT, "Mac (1)").click()
time.sleep(2)

# Locate dropdown
dropdown = Select(driver.find_element(By.ID, "input-sort"))

# Print all options
options = dropdown.options
for option in options:
    print(option.text)

# Select 5th option (index starts at 0)
dropdown.select_by_index(4)

time.sleep(3)
driver.quit()

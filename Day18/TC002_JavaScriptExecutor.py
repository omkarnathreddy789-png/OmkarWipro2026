from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.amazon.in")

time.sleep(3)

# Scroll down by 900 pixels
driver.execute_script("window.scrollBy(0, 900)")

time.sleep(2)

# Scroll to bottom of page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

time.sleep(3)
driver.quit()

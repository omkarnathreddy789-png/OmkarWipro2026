from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Google Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# 1. Open Google
driver.get("https://www.google.com")
print("Page 1 Title:", driver.title)

time.sleep(2)

# 2. Navigate to another page on Google (About Google link)
driver.find_element(By.LINK_TEXT, "About").click()
time.sleep(2)
print("Page 2 Title:", driver.title)

# 3. Back
driver.back()
time.sleep(2)
print("After Back:", driver.title)

# 4. Forward
driver.forward()
time.sleep(2)
print("After Forward:", driver.title)

# 5. Refresh
driver.refresh()
time.sleep(2)
print("After Refresh:", driver.title)

# 6. Close browser
driver.quit()

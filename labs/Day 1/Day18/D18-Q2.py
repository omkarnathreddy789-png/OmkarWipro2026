from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")

wait = WebDriverWait(driver, 10)

# ✅ Switch to iframe safely
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))

# ✅ Locate editor
editor = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))

# ✅ Click using JavaScript (bypasses overlay issue)
driver.execute_script("arguments[0].click();", editor)

# ✅ Clear properly
editor.send_keys(Keys.CONTROL + "a")
editor.send_keys(Keys.BACKSPACE)

# ✅ Type text
editor.send_keys("Iframe handled successfully!")

# Back to main page
driver.switch_to.default_content()

# Open new tab
driver.execute_script("window.open('https://www.google.com');")

windows = driver.window_handles

# Switch and print titles
for w in windows:
    driver.switch_to.window(w)
    print("Window Title:", driver.title)

# Close child window
driver.switch_to.window(windows[1])
driver.close()

# Return to parent
driver.switch_to.window(windows[0])
print("Returned to:", driver.title)

time.sleep(2)
driver.quit()

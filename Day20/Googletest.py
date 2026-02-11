from Driverfactory import get_driver
import time

print("Script started")

driver = get_driver("chrome")

print("Opening Google")
driver.get("https://www.google.com")

print("Page title is:", driver.title)

time.sleep(5)

driver.quit()
print("Script finished")

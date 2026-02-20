from datetime import datetime


import pytest
import configparser
import os

from Capstone_Project.utilities.driver_factory import get_driver
from Capstone_Project.utilities.logger import get_logger

logger = get_logger()


# ----------- SUITE START / END -----------

def pytest_sessionstart(session):
    logger.info("========== TEST SUITE STARTED ==========")


def pytest_sessionfinish(session, exitstatus):
    logger.info("========== TEST SUITE FINISHED ==========")
    logger.info(f"Total Tests Collected: {session.testscollected}")

# ----------- TEST START / END -----------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_protocol(item, nextitem):
    logger.info(f"------ Test Started: {item.name} ------")
    yield
    logger.info(f"------ Test Finished: {item.name} ------\n")


# ----------- SCREENSHOT ON FAILURE -----------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Take screenshot only if test FAILED in call phase
    if rep.when == "call" and rep.failed:

        driver = item.funcargs.get("setup", None)

        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)

            logger.error(f"Test Failed: {item.name}")
            logger.error(f"Screenshot saved at: {file_path}")
# ----------- SETUP / TEARDOWN -----------
browsers = ["chrome", "firefox"]
@pytest.fixture(scope="function",params=browsers)
def setup(request):
    browser_name = request.param
    logger.info(f"Browser Setup Started: {browser_name}")

    driver = get_driver(browser_name)  # Pass browser_name to your driver_factory

    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "config/config.ini"))
    base_url = config["DEFAULT"]["base_url"]

    driver.get(base_url)
    yield driver

    logger.info(f"Browser Teardown Started: {browser_name}")
    driver.quit()
    logger.info(f"Browser Closed Successfully: {browser_name}\n")

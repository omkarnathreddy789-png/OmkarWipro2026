import pytest
import configparser
import os
from Capstone_Project.utilities.driver_factory import get_driver
from Capstone_Project.utilities.logger import get_logger

logger = get_logger()


# 1️⃣ Add CLI option for browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,  # fallback to config.ini if not provided
        help="Browser to run tests: chrome, firefox, edge"
    )


# 2️⃣ Fixture to set up driver
@pytest.fixture(scope="function")
def setup(request):
    cli_browser = request.config.getoption("--browser")

    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "../config/config.ini"))

    if cli_browser:
        config["DEFAULT"]["browser"] = cli_browser.lower()

    browser_name = config["DEFAULT"]["browser"].lower()
    logger.info(f"Browser Setup Started: {browser_name}")

    driver = get_driver()  # reads browser from config

    base_url = config["DEFAULT"]["base_url"]
    driver.get(base_url)

    yield driver

    logger.info("Browser Teardown Started")
    driver.quit()
    logger.info("Browser Closed Successfully\n")

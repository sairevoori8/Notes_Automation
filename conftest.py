
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from config.environment import config
import os
import allure


@pytest.fixture(scope="function")
def driver():

    options = Options()

    # Disable notifications & popups
    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.popups": 0,
    }
    options.add_experimental_option("prefs", prefs)

    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(config.get("implicit_wait"))

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            screenshots_dir = "reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            screenshot_path = os.path.join(
                screenshots_dir,
                f"{item.name}.png"
            )

            driver.save_screenshot(screenshot_path)

            allure.attach.file(
                screenshot_path,
                name=item.name,
                attachment_type=allure.attachment_type.PNG
            )
import os
from datetime import datetime

import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from config.environment import config


@pytest.fixture(scope="function")
def driver():

    chrome_options = Options()

    # Browser Preferences
    prefs = {
    "profile.default_content_setting_values.notifications": 2,
    "profile.default_content_setting_values.popups": 0,
    "profile.managed_default_content_settings.images": 2
    }

    chrome_options.add_experimental_option("prefs", prefs)

    # Common Browser Arguments
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")

    # Headless / Docker Settings
    if config.get("headless"):

        # Headless mode
        chrome_options.add_argument("--headless=new")
        
        # Docker/Linux stability
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Rendering stability
        chrome_options.add_argument("--disable-gpu")

        # Responsive layout
        chrome_options.add_argument("--window-size=1920,1080")

        # Extra stability
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument(
            "--disable-blink-features=AutomationControlled"
        )
        chrome_options.add_argument(
            "--disable-features=VizDisplayCompositor"
        )

    execution_mode = config.get("execution_mode")

    # GRID Execution
    if execution_mode == "grid":

        print(
            f"\nRunning in GRID mode -> "
            f"{config.get('grid_url')}"
        )

        driver = webdriver.Remote(
            command_executor=config.get("grid_url"),
            options=chrome_options
        )

    # LOCAL Execution
    else:

        print("\nRunning in LOCAL mode")

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=chrome_options
        )

    # Waits
    driver.implicitly_wait(
        config.get("implicit_wait")
    )

    # Window Size
    driver.set_window_size(1920, 1080)

    yield driver

    print("\nClosing browser...")
    driver.quit()


# Screenshot Capture on Failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    # Capture screenshot if test fails
    if report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            screenshots_dir = "reports/screenshots"
            os.makedirs(
                screenshots_dir,
                exist_ok=True
            )

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            screenshot_path = os.path.join(
                screenshots_dir,
                f"{item.name}_{timestamp}.png"
            )

            try:

                driver.save_screenshot(
                    screenshot_path
                )

                allure.attach.file(
                    screenshot_path,
                    name=f"{item.name}_failure",
                    attachment_type=allure.attachment_type.PNG
                )

                print(
                    f"\nScreenshot saved -> "
                    f"{screenshot_path}"
                )

            except Exception as e:

                print(
                    f"\nFailed to capture screenshot: {e}"
                )
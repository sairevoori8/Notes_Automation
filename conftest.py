import pytest
import os
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config.environment import config


@pytest.fixture(scope="function")
def driver():

    options = Options()

    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.popups": 0,
    }

    options.add_experimental_option("prefs", prefs)

    # Common Browser Arguments
   
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")

  
    # Headless / Docker Stability

    if config.get("headless"):
        # Headless mode
        options.add_argument("--headless=new")

        # Docker/Linux stability
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Rendering stability
        options.add_argument("--disable-gpu")

        # IMPORTANT for responsive layout
        options.add_argument("--window-size=1920,1080")

        # Extra stability
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")

    execution_mode = config.get("execution_mode")
    if execution_mode == "grid":
        
        print(f"Running in GRID mode. Connecting to {config.get('grid_url')}")
        driver = webdriver.Remote(
            command_executor=config.get("grid_url"),
            options=options
        )

    else:
        print("Running in LOCAL mode.")
        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=options
        )

  
    # Waits
    driver.implicitly_wait(
        config.get("implicit_wait")
    )

    # Important for headless mode
    driver.set_window_size(1920, 1080)

    yield driver

    driver.quit()

# Capture screenshot on failure
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
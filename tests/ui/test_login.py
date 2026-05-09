import pytest
from pages.login_page import LoginPage
from config.environment import config
import selenium.webdriver.support.ui

# Test to login
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.ts
def test_valid_login(driver):

    login_page = LoginPage(driver)

    login_page.load()
    login_page.navigate_to_login()
    login_page.login(
        config.get("email"),
        config.get("password")
    )

    assert login_page.is_login_successful()

# Test to login with invalid credentials
@pytest.mark.ui
@pytest.mark.smoke
def test_login_invalid_credentials(driver):

    login_page = LoginPage(driver)

    login_page.load()
    login_page.navigate_to_login()

    login_page.login(
        "invalid@gmail.com",
        "Wrong123"
    )

    error_message = login_page.get_error_message()

    assert error_message is not None, "Error message not displayed"
    assert "Incorrect" in error_message, "Incorrect error message"
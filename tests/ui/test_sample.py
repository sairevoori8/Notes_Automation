import pytest

# Basic test to verify app launch
@pytest.mark.sanity
def test_launch_app(driver):
    driver.get("https://practice.expandtesting.com/notes/app")
    assert "notes" in driver.title.lower()
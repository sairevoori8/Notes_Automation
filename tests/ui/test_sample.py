import pytest

@pytest.mark.ui
def test_launch_app(driver):
    driver.get("https://practice.expandtesting.com/notes/app")
    assert "notes" in driver.title.lower()
import pytest
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from config.environment import config
import time

@pytest.mark.ui
@pytest.mark.smoke
def test_create_note_valid(driver):

    login_page = LoginPage(driver)
    notes_page = NotesPage(driver)

    login_page.load()
    login_page.navigate_to_login()
    login_page.login(
        config.get("email"),
        config.get("password")
    )

    title = "Capstone"
    description = "Automation Note"

    notes_page.click_add_note()
    notes_page.create_note(title, description)

    assert notes_page.is_note_created(title), "Note creation failed"

@pytest.mark.ui
@pytest.mark.regression

def test_create_note_empty_fields(driver):

    login_page = LoginPage(driver)
    notes_page = NotesPage(driver)

    login_page.load()
    login_page.navigate_to_login()
    login_page.login(
        config.get("email"),
        config.get("password")
    )

    notes_page.click_add_note()

    notes_page.click_create()

    title_error = notes_page.get_title_error()
    desc_error = notes_page.get_description_error()

    assert "required" in title_error.lower(), "Title validation missing"
    assert "required" in desc_error.lower(), "Description validation missing"

@pytest.mark.ui
@pytest.mark.regression

def test_mark_note_as_completed(driver):

    login_page = LoginPage(driver)
    notes_page = NotesPage(driver)

    login_page.load()
    login_page.navigate_to_login()

    login_page.login(
        config.get("email"),
        config.get("password")
    )

    title = "Capstone23"
    description = "Automation Note33"

    notes_page.click_add_note()
    notes_page.create_note(title, description)

    assert notes_page.is_note_created(title), \
        "Note creation failed"

    notes_page.click_note_checkbox(title)

    assert notes_page.is_note_completed(title), \
        "Note was not marked as completed"



@pytest.mark.ui
@pytest.mark.regression

def test_edit_existing_note(driver):

    login_page = LoginPage(driver)
    notes_page = NotesPage(driver)

    login_page.load()
    login_page.navigate_to_login()

    login_page.login(
        config.get("email"),
        config.get("password")
    )

    timestamp = int(time.time())

    old_title = f"Capstone_{timestamp}"
    old_description = f"Automation_Note_{timestamp}"

    new_title = f"Updated_Capstone_{timestamp}"
    new_description = f"Updated_Automation_Note_{timestamp}"

    notes_page.click_add_note()

    notes_page.create_note(
        old_title,
        old_description
    )

    assert notes_page.is_note_created(old_title), \
        "Original note creation failed"

    notes_page.click_edit(old_title)

    notes_page.update_note(
        new_title,
        new_description
    )

    assert notes_page.is_note_created(new_title), \
        "Note edit failed"
    

@pytest.mark.ui
@pytest.mark.regression

def test_delete_existing_note(driver):

    login_page = LoginPage(driver)
    notes_page = NotesPage(driver)

    login_page.load()
    login_page.navigate_to_login()

    login_page.login(
        config.get("email"),
        config.get("password")
    )

    timestamp = int(time.time())

    title = f"Delete_Note_{timestamp}"
    description = f"Delete_Description_{timestamp}"

    notes_page.click_add_note()

    notes_page.create_note(
        title,
        description
    )

    assert notes_page.is_note_created(title), \
        "Note creation failed"

    notes_page.click_delete(title)

    notes_page.confirm_delete()

    assert notes_page.is_note_deleted(title), \
        "Note was not deleted"
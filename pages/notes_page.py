from allure import title
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait

class NotesPage(BasePage):

    # ---------- Locators ----------

    # Add Note Button
    ADD_NOTE_BUTTON = (By.XPATH, "//button[@data-testid='add-new-note']")

    # Modal Fields
    TITLE_INPUT = (By.XPATH, "//input[@data-testid='note-title']")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@data-testid='note-description']")
    CREATE_BUTTON = (By.XPATH, "//button[@data-testid='note-submit']")

    TITLE_ERROR = (
    By.XPATH,
    "//input[@data-testid='note-title']/following-sibling::div[contains(@class,'invalid-feedback')]"
    )

    DESCRIPTION_ERROR = (
        By.XPATH,
        "//textarea[@data-testid='note-description']/following-sibling::div[contains(@class,'invalid-feedback')]"
    )
    CONFIRM_DELETE_BUTTON = (
         By.XPATH,
        "//button[@data-testid='note-delete-confirm']"
    )
    # Note Card (Dynamic)
    def note_title(self, title):
        return (
            By.XPATH,
            f"//div[@data-testid='note-card-title'][text()='{title}']"
        )

    # ---------- Actions ----------

    def click_add_note(self):
        self.click(self.ADD_NOTE_BUTTON)

    def enter_title(self, title):
        self.enter_text(self.TITLE_INPUT, title)

    def enter_description(self, description):
        self.enter_text(self.DESCRIPTION_INPUT, description)

    def click_create(self):
        self.click(self.CREATE_BUTTON)

    def create_note(self, title, description):
        self.enter_title(title)
        self.enter_description(description)
        self.click_create()

    # ---------- Validations ----------

    def is_note_created(self, title):
        return self.is_visible(self.note_title(title))

    def get_title_error(self):
        return self.get_text(self.TITLE_ERROR)

    def get_description_error(self):
        return self.get_text(self.DESCRIPTION_ERROR)
    

    def note_checkbox(self, title):
        return (
            By.XPATH,
            f"//div[@data-testid='note-card'][.//div[@data-testid='note-card-title'][normalize-space()='{title}']]//input[@data-testid='toggle-note-switch']"
        )


    def click_note_checkbox(self, title):

        locator = self.note_checkbox(title)

        for _ in range(3):
            try:
                checkbox = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(locator)
                )

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    checkbox
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    checkbox
                )

                return

            except StaleElementReferenceException:
                continue

        raise Exception(f"Failed to click checkbox for note: {title}")
    
    def is_note_completed(self, title):

        card = self.wait.until(
            EC.presence_of_element_located(
                self.note_card(title)
            )
        )

        background_color = card.value_of_css_property(
            "background-color"
        )

        return background_color == "rgba(248, 249, 250, 1)" 
        
    def note_card(self, title):
        return (
            By.XPATH,
            f"//div[@data-testid='note-card'][.//div[@data-testid='note-card-title'][normalize-space()='{title}']]"
        )
    
    def edit_button(self, title):
        return (
            By.XPATH,
            f"//div[@data-testid='note-card'][.//div[@data-testid='note-card-title'][normalize-space()='{title}']]//button[@data-testid='note-edit']"
        )
    def click_edit(self, title):
        self.click(self.edit_button(title))
        
    def update_note(self, new_title, new_description):

        self.enter_text(self.TITLE_INPUT, new_title)
        self.enter_text(self.DESCRIPTION_INPUT, new_description)

        self.click(self.CREATE_BUTTON)

    def delete_button(self, title):
        return (
            By.XPATH,
            f"//div[@data-testid='note-card'][.//div[@data-testid='note-card-title'][normalize-space()='{title}']]//button[@data-testid='note-delete']"
        )
    def confirm_delete(self):
        self.click(self.CONFIRM_DELETE_BUTTON)
    def is_note_deleted(self, title):

        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: len(
                    d.find_elements(*self.note_title(title))
                ) == 0
            )

            return True

        except:
            return False
        
    def click_delete(self, title):
        self.click(self.delete_button(title))

    def delete_button(self, title):
        return (
            By.XPATH,
            f"//div[@data-testid='note-card'][.//div[@data-testid='note-card-title'][normalize-space()='{title}']]//button[@data-testid='note-delete']"
        )
    def note_description(self, description):
        return (
            By.XPATH,
            f"//p[@data-testid='note-card-description'][contains(text(),'{description}')]"
        )
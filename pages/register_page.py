from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import RegisterPageLocators


class RegisterPage(BasePage):
    def verify_register_page(self):
        WebDriverWait(self.driver, 20).until(
            EC.title_is, ("Utwórz nowe konto klienta | Wiosna 2022 na eobuwie.pl")
        )

    def fill_name(self, name):
        el = self.driver.find_element(*RegisterPageLocators.NAME_INPUT)
        el.send_keys(name)

    def fill_lastname(self, lastname):
        el = self.driver.find_element(*RegisterPageLocators.LASTNAME_INPUT)
        el.send_keys(lastname)

    def fill_email(self, email):
        el = self.driver.find_element(*RegisterPageLocators.EMAIL_INPUT)
        el.send_keys(email)

    def fill_password(self, password):
        el = self.driver.find_element(*RegisterPageLocators.PASSWORD_INPUT)
        el.send_keys(password)

    def confirm_password(self, password):
        el = self.driver.find_element(*RegisterPageLocators.CONFIRMATION_INPUT)
        el.send_keys(password)

    def accept_policy(self):
        self.driver.find_element(*RegisterPageLocators.POLICY_CHECKBOX).click()

    def create_account(self):
        self.driver.find_element(*RegisterPageLocators.CREATE_ACCOUNT_BTN).click()

    def verify_visible_errors(self, number_of_errors, error_texts):
        error_notices = self.driver.find_elements(
            *RegisterPageLocators.REGISTRATION_ERRORS
        )
        visible_error_notices = [error for error in error_notices if error.is_displayed]
        assert len(visible_error_notices) == number_of_errors
        error_messages = [
            error.get_attribute("innerText") for error in visible_error_notices
        ]
        print(error_messages)
        for message in error_messages:
            assert message in error_texts

from pages.base_page import BasePage
from locators import RegisterPageLocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage(BasePage):
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

    def verify_visible_errors(self, number_of_errors, errors_texts):
        error_notices = self.driver.find_elements(*RegisterPageLocators.REGISTRATION_ERRORS)
        visible_error_notices = []
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)

        print(len(visible_error_notices))
        assert len(visible_error_notices) == number_of_errors
        errors_text_fact = []
        for i in range (len(visible_error_notices)):
            errors_text_fact.append(visible_error_notices[i].get_attribute("innerText"))
            print(errors_text_fact)
            print(errors_texts)
            assert errors_text_fact == errors_texts

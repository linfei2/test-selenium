from selenium.webdriver.common.by import By


class HomePageLocators:
    ACCEPT_BANNER = (By.XPATH, "//div[@class='e-consents-alert__actions']/button[1]")
    SIGN_IN_BTN = (By.XPATH, "//a[@title='Zarejestruj']")


class RegisterPageLocators:
    NAME_INPUT = (By.ID, "firstname")
    LASTNAME_INPUT = (By.ID, "lastname")
    EMAIL_INPUT = (By.ID, "email_address")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRMATION_INPUT = (By.ID, "confirmation")
    POLICY_CHECKBOX = (By.XPATH, "//label[@class='checkbox-wrapper__label']")
    CREATE_ACCOUNT_BTN = (By.ID, "create-account")
    REGISTRATION_ERRORS = (By.XPATH, "//span[@class='help-block form-error']")

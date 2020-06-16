from selenium.webdriver.common.by import By

class HomePageLocators():
    ACCEPT_BANNER = (By.XPATH, '//*[@id="top"]/body/div[6]/div/div/div/section/button[2]')
    SIGN_IN_BTN = (By.XPATH,'//*[@id="top"]/body/header/div[3]/div/div/div[2]/div/a[6]')

class RegisterPageLocators():
    NAME_INPUT = (By.ID,'firstname')
    LASTNAME_INPUT = (By.ID, 'lastname')
    EMAIL_INPUT = (By.ID, 'email_address')
    PASSWORD_INPUT = (By.ID, 'password')
    CONFIRMATION_INPUT = (By.ID, 'confirmation')
    POLICY_CHECKBOX = (By.XPATH, '//*[@id="top"]/body/div[3]/div/div/form/div[7]/label')
    CREATE_ACCOUNT_BTN = (By.ID, 'create-account')
    REGISTRATION_ERRORS = (By.XPATH, '//*[@id="top"]/body/div[3]/div/div/form/div[3]/span')

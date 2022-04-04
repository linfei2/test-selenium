from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators


class HomePage(BasePage):
    def click_accept_banner(self):
        el = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(HomePageLocators.ACCEPT_BANNER)
        )
        el.click()
        sleep(1)

    def click_sign_in(self):
        el = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(HomePageLocators.SIGN_IN_BTN)
        )
        el.click()

    def _verify_page(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(HomePageLocators.ACCEPT_BANNER)
        )
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(HomePageLocators.ACCEPT_BANNER)
        )
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(HomePageLocators.SIGN_IN_BTN)
        )
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(HomePageLocators.SIGN_IN_BTN)
        )
        assert (
            "Sklep internetowy eobuwie.pl • Modne buty, akcesoria i torebki online | Wiosna 2022 na eobuwie.pl"
            in self.driver.title
        )
        print("Weryfikacja strony HomePage")

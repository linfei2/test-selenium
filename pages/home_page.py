from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators

class HomePage(BasePage):
    def click_accept_banner(self):
        el = self.driver.find_element(*HomePageLocators.ACCEPT_BANNER)
        el.click()

    def click_sign_in(self):
        el = self.driver.find_element(*HomePageLocators.SIGN_IN_BTN)
        el.click()

    def _verify_page(self):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(HomePageLocators.ACCEPT_BANNER))
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(HomePageLocators.ACCEPT_BANNER))
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(HomePageLocators.SIGN_IN_BTN))
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(HomePageLocators.SIGN_IN_BTN))
        assert "Modne buty damskie, męskie, dziecięce oraz torebki" in self.driver.title
        print("Weryfikacja strony HomePage")

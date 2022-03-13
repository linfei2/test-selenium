from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
import unittest
import time

class RegistrationTest(BaseTest):
    def test_incorrect_email(self):
        hp = HomePage(self.driver)
        hp.click_accept_banner()
        hp.click_sign_in()

        rp = RegisterPage(self.driver)
        rp.fill_name('Jan')
        rp.fill_lastname('Kowalski')
        rp.fill_email('jkowalski.pl')
        rp.fill_password('H@slo123')
        rp.confirm_password('H@slo123')
        rp.accept_policy()
        rp.create_account()
        rp.verify_visible_errors(1, ['Wprowadzono niepoprawny adres e-mail'])


if __name__=='__main__':
    unittest.main(verbosity=2)

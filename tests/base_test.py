import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.eobuwie.com.pl/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.save_screenshot("screenshot.png")
        self.driver.quit()

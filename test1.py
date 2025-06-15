import os

import allure
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Test(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    @allure.title("Basic test")
    def test_1(self):
        email = os.environ.get("EMAIL")
        password = os.environ.get("PASSWORD")
        self.driver.find_element(By.ID, "reg_email").send_keys(email)
        self.driver.find_element(By.ID, "reg_password").send_keys(password)
        myAcc = self.driver.find_element(By.ID, "menu-item-22")
        self.assertTrue(myAcc.is_enabled())

    def tearDown(self):
        self.driver.quit()

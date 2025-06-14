import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://seleniumdemo.com/")

    def test_1(self):
        myAcc = self.driver.find_element(By.ID, "menu-item-22")
        self.assertTrue(myAcc.is_displayed())

    def tearDown(self):
        self.driver.quit()
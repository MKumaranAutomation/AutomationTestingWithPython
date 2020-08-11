from selenium import webdriver
import unittest

class GoogleSearchTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('../Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_Search_GoogleCompany(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Google Company")
        self.driver.find_element_by_name("btnK").click()

    def test_Search_MicrosoftCompany(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Google Company")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("The Test has been completed...")
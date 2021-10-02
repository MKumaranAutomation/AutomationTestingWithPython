import unittest
from selenium import webdriver


class GoogleSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"/Volumes/D Drive/TopTechGurus/Trainings/GoogleTests/AutomationTestingWithPython/Drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_Search_GoogleCompany(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Google Company")
        self.driver.find_element_by_name("btnK").click()
        assertEqual("Tutorialspoint", "Tutorialspoint")

    def test_Search_MicrosoftCompany(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Microsoft Company")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("The Test has been completed...")


if __name__ == '__main__':
    unittest.main()

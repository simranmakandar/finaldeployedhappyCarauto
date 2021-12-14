import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class validateCategories(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Safari()
    def test_ll(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")
        elem = driver.find_element_by_link_text("Categories")
        elem.click()
        time.sleep(3)
        #assert "Categories Show"
        try:
            # attempt to find the Categories header - if found, categories show
            elem = driver.find_element_by_id("categories-header")
            assert True
        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False
        time.sleep(3)
def tearDown(self):
    self.driver.close()
if __name__ == "__main__":
    unittest.main()
import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class validateCategories(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Safari()
    def test_ll(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")
        elem = driver.find_element_by_link_text("All Products")
        elem.click()
        time.sleep(3)
        #assert "Products Show"
        try:
            # attempt to find the Products header, if found 'successful'
            elem = driver.find_element_by_id("products-header")
            assert True
        except NoSuchElementException:
            self.fail("Unable to find Products page")
            assert False
        time.sleep(3)
def tearDown(self):
    self.driver.close()
if __name__ == "__main__":
    unittest.main()
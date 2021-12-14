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
        elem = driver.find_element_by_id("searchbar")
        elem.send_keys('replacement')
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        #assert "Search Results Work"
        try:
            # attempt to find the 'Replacement Radiator' product - if found, search works
            elem = driver.find_element_by_link_text("Replcement Radiator")
            assert True
        except NoSuchElementException:
            self.fail("Search may not be working or product does not exist")
            assert False
        time.sleep(3)
def tearDown(self):
    self.driver.close()
if __name__ == "__main__":
    unittest.main()
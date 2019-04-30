from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from GoogleMaps.Parameters.parameters import Parameters
from GoogleMaps.Pages.googleMaps import GoogleMaps
import unittest
import HtmlTestRunner


class QaTask(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="./GoogleMaps/drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.set_page_load_timeout(10)
        cls.driver.implicitly_wait(10)

    def test_is_page_up(self):

        # if page loads within load timeout verifies title and link
        # asserts page status at the end
        pagestatus = "page loaded"
        try:
            self.driver.get(Parameters.url)
            self.assertIn('Google Maps', self.driver.title)
            self.assertIn('https://www.google.com/maps', self.driver.current_url)
        except TimeoutException as ex:
            pagestatus = ex.msg

        self.assertEqual("page loaded", pagestatus)

    def test_longest_direction(self):

        maps = GoogleMaps(self.driver)

        maps.click_get_directions()
        maps.enter_directions(Parameters.current_location, Parameters.destination)
        maps.click_car()
        maps.click_options()
        maps.click_avoid_highways()
        maps.select_route(maps.find_longest_route())

    def test_trip_details(self):

        maps = GoogleMaps(self.driver)

        maps.click_details()
        distance, duration = maps.get_trip_details()

        self.assertIsNotNone(distance)
        self.assertIsNotNone(duration)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner("./GoogleMaps/reports"))


from GoogleMaps.Locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GoogleMaps:

    def __init__(self, driver):
        self.driver = driver
        self.search_textbox_id = Locators.search_textbox_id
        self.search_button_id = Locators.search_button_id
        self.get_directions_button_id = Locators.get_directions_button_id
        self.directions_inputbox1_xpath = Locators.directions_inputbox1_xpath
        self.directions_inputbox2_xpath = Locators.directions_inputbox2_xpath
        self.car_button_xpath = Locators.car_button_xpath
        self.options_button_xpath = Locators.options_button_xpath
        self.avoid_highways_checkbox_xpath = Locators.avoid_highways_checkbox_xpath
        self.details_button_xpath = Locators.details_button_xpath
        self.all_routes_xpath = Locators.all_routes_xpath
        self.details_distance_xpath = Locators.details_distance_xpath
        self.details_duration_xpath = Locators.details_duration_xpath

    def enter_search_text(self, search_text):
        self.driver.find_element_by_id(self.search_textbox_id).send_keys(search_text)

    def click_search(self):
        self.driver.find_element_by_id(self.search_button_id).click()

    def click_get_directions(self):
        self.driver.find_element_by_id(self.get_directions_button_id).click()

    def enter_directions(self, directionFrom, directionTo):
        self.driver.find_element_by_xpath(self.directions_inputbox1_xpath).send_keys(directionFrom)
        self.driver.find_element_by_xpath(self.directions_inputbox2_xpath).send_keys(directionTo)

    def click_car(self):
        self.driver.find_element_by_xpath(self.car_button_xpath).click()

    def click_options(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.options_button_xpath)))
        self.driver.find_element_by_xpath(self.options_button_xpath).click()

    def click_avoid_highways(self):
        self.driver.find_element_by_xpath(self.avoid_highways_checkbox_xpath).click()

    def find_longest_route(self):
        # load routes elements into list
        list_of_routes = self.driver.find_elements_by_xpath(self.all_routes_xpath)

        # find longest route index from the list
        longest_route_index = 0

        for position in range(len(list_of_routes)):
            if list_of_routes[position].text.split(' ')[0] > list_of_routes[longest_route_index].text.split(' ')[0]:
                longest_route_index = position

        return longest_route_index

    def select_route(self, index):
        # click on element in list with given index
        # if index 0 element is already selected so skip
        if index != 0:
            self.driver.find_elements_by_xpath(self.all_routes_xpath)[index].click()

    def click_details(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.details_button_xpath)))
        self.driver.find_element_by_xpath(self.details_button_xpath).click()

    def get_trip_details(self):
        # if distance and duration are displayed will return them, if not returns None
        distance = None
        duration = None
        if self.driver.find_element_by_xpath(self.details_duration_xpath).is_displayed():
            duration = self.driver.find_element_by_xpath(self.details_duration_xpath).text
        if self.driver.find_element_by_xpath(self.details_distance_xpath).is_displayed():
            distance = self.driver.find_element_by_xpath(self.details_distance_xpath).text
        print(duration, distance)
        return duration, distance

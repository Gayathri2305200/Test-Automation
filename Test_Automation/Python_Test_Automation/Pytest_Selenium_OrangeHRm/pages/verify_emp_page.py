from locators.locators import Locators
from utilities.read_config import ReadConfig
from utilities.utility_methods import *


class VerifyEmpPage:
    FULLNAME = ReadConfig.get_firstname() + ReadConfig.get_lastname()

    def __init__(self, driver):
        self.driver = driver

    def click_pim_button(self):
        locate_by_xpath(self.driver, Locators.pim_button).click()

    def set_emp_name(self):
        locate_by_xpath(self.driver, Locators.employee_name).send_keys(self.FULLNAME)

    def click_search_button(self):
        locate_by_xpath(self.driver, Locators.search_button).click()

    def verify_emp(self):
        webdriver_wait_by_xpath(self.driver, 10, Locators.no_of_records)
        countOfRecords = locate_by_xpath(self.driver, Locators.no_of_records).text
        return countOfRecords

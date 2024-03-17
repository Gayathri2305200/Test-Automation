from locators.locators import Locators
from utilities.utility_methods import *


class PIMPage:

    def __init__(self, driver):
        self.driver = driver

    def click_pim_button(self):
        locate_by_xpath(self.driver, Locators.pim_button).click()
        pim = locate_by_xpath(self.driver, Locators.pim_button_text).text
        return pim

    def click_add_emp_button(self):
        self.driver.implicitly_wait(20)
        locate_by_xpath(self.driver, Locators.add_emp).click()
        pim = locate_by_xpath(self.driver, Locators.title).text
        return pim

from utilities.utility_methods import *
from utilities.readconfig import ReadConfig
from locators.locators import Locators


class EmployeeInfo:


    def __init__(self, driver):
        self.driver = driver

    def set_firstname(self):
        locate_by_name(self.driver,Locators.firstname).send_keys(ReadConfig.get_firstname())

    def set_lastname(self):
        locate_by_name(self.driver, Locators.lastname).send_keys(ReadConfig.get_lastname())

    def click_create_login_details_button(self):
        locate_by_xpath(self.driver, Locators.create_login_details_button).click()

    def add_username(self):
        locate_by_xpath(self.driver, Locators.add_username).send_keys(ReadConfig.get_firstname())

    def add_password(self):
        locate_by_xpath(self.driver, Locators.add_password).send_keys(ReadConfig.get_password())

    def confirm_password(self):
        locate_by_xpath(self.driver, Locators.confirm_password).send_keys(ReadConfig.get_password())

    def click_save_button(self):
        locate_by_xpath(self.driver, Locators.save_button).click()

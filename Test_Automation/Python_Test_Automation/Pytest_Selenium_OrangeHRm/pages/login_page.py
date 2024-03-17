from locators.locators import Locators
from utilities.read_config import ReadConfig
from utilities.utility_methods import *


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def set_username(self):
        webdriver_wait_by_name(self.driver, 20, Locators.username)
        locate_by_name(self.driver, Locators.username).send_keys(ReadConfig.get_username())

    def set_password(self):
        locate_by_name(self.driver, Locators.password).send_keys(ReadConfig.get_password())

    def click_login_button(self):
        locate_by_xpath(self.driver, Locators.login_button).click()

    def verify_title(self):
        self.driver.implicitly_wait(10)
        dashboard = locate_by_xpath(self.driver, Locators.title).text
        return dashboard

import time
from locators import locators

from utilities.utility_methods import locate_by_xpath


class Remove_Item_Page:
    locator = locators.Locators()

    def __init__(self, driver):
        self.driver = driver

    def click_remove(self, remove):
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        locate_by_xpath(self.driver, locators.get_path_by_text(remove)).click()

    def confirm_remove(self, remove):
        time.sleep(10)
        locate_by_xpath(self.driver, Remove_Item_Page.locator.remove_button).click()

    def verify_cart(self, cart):
        time.sleep(5)
        ver = locate_by_xpath(self.driver, Remove_Item_Page.locator.missing_cart).text
        assert ver == cart

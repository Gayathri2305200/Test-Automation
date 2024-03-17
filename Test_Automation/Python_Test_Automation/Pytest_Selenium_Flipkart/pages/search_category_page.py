import time
from selenium.webdriver import Keys
from utilities.utility_methods import *
from locators import locators


class Search_Category_Page:
    locator = locators.Locators()

    def __init__(self, driver):
        self.driver = driver

    def search_category(self, title):
        locate_by_name(self.driver, Search_Category_Page.locator.search_bar).send_keys(title)
        locate_by_name(self.driver, Search_Category_Page.locator.search_bar).send_keys(Keys.ENTER)
        print(self.driver.title)
        assert title in self.driver.title

    def select_brand(self, brand):
        try:
            mobile_brand = locate_by_xpath(self.driver, locators.get_path_by_sibling(brand))
            mobile_brand.click()
        except Exception:
            locate_by_xpath(self.driver, locators.get_path_by_text("Brand")).click()
            time.sleep(10)
            mobile_brand = locate_by_xpath(self.driver, locators.get_path_by_sibling(brand))
            mobile_brand.click()
        time.sleep(20)

    def sort_by_newest(self, sort_by):
        locate_by_xpath(self.driver, locators.get_path_by_text(sort_by)).click()

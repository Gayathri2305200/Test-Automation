import time
from utilities.utility_methods import *
from locators import locators


class Add_to_cart_Page:
    locator = locators.Locators()

    def __init__(self, driver):
        self.driver = driver

    def select_mobile(self, mobile):
        # mobile=locate_by_xpath(self.driver, Add_to_cart_Page.locator.get_path_by_contains_text(mobile))
        # try:
        #     webdriver_wait_by_xpath(self.driver,30,Add_to_cart_Page.locator.get_path_by_contains_text(mobile)).click()
        #
        # except StaleElementReferenceException:
        #     mobile.click()
        # webdriver_wait_by_xpath(self.driver, 30, Add_to_cart_Page.locator.get_path_by_contains_text(mobile)).click()
        time.sleep(5)
        locate_by_xpath(self.driver, locators.get_path_by_contains_text(mobile)).click()
        webdriver_waits(self.driver, 10)
        first_tab = self.driver.current_window_handle
        tabs = self.driver.window_handles
        for i in tabs:
            if i != first_tab:
                self.driver.switch_to.window(i)
                break
        print(self.driver.title)
        assert mobile in self.driver.title

    def click_addtocart(self):
        time.sleep(5)
        # webdriver_waits(self.driver,20)
        self.driver.execute_script("window.scrollTo(0,100);")
        locate_by_xpath(self.driver, Add_to_cart_Page.locator.add_to_cart).click()
        print("add")
        # action = ActionChains(self.driver)
        # # perform the operation
        # action.move_to_element(atc).click().perform()
        # self.driver.execute_script("window.scrollTo(0,100);")

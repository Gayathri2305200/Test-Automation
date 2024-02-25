from locators.locators import Locators
from utilities.read_cofigurations import ReadConfig
from utilities.utility_methods import locate_by_class


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    def home_page(self, title):
        print("homepage")
        self.driver.get(ReadConfig.get_baseURL())
        try:
            locate_by_class(self.driver, Locators.dismiss).click()
        except Exception:
            pass
        print(self.driver.title)
        assert title in self.driver.title

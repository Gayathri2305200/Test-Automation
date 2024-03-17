from utilities.read_config import ReadConfig


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    def home_page(self, expected_title):
        print(ReadConfig.get_baseURL())
        self.driver.get(ReadConfig.get_baseURL())
        assert self.driver.title == expected_title

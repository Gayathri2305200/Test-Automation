import configparser

configurations = configparser.ConfigParser()
configurations.read(
    r'C:\Users\kurap\OneDrive\Desktop\Testing\Test_Automation\Python_Test_Automation\Pytest_Selenium_OrangeHRm\configurations\config.ini')


class ReadConfig:
    @staticmethod
    def get_browser():
        url = configurations.get('basic info', 'browser')
        return url

    @staticmethod
    def get_baseURL():
        url = configurations.get('basic info', 'baseURL')
        return url

    @staticmethod
    def get_firstname():
        url = configurations.get('user info', 'firstname')
        return url

    @staticmethod
    def get_lastname():
        url = configurations.get('user info', 'lastname')
        return url

    @staticmethod
    def get_username():
        url = configurations.get('basic info', 'username')
        return url

    @staticmethod
    def get_password():
        url = configurations.get('basic info', 'password')
        return url

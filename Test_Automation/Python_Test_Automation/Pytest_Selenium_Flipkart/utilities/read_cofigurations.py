import configparser

configurations = configparser.ConfigParser()
configurations.read(r"C:\Users\Gayathri_Kurapati\Desktop\Test Automation\Pytest_Selenium\configurations\config.ini")


class ReadConfig:
    @staticmethod
    def get_browsers():
        browsers= [configurations.get("browsers","browser1"),configurations.get("browsers","browser2")]
        return browsers

    @staticmethod
    def get_baseURL():
        url = configurations.get('basic info', 'baseURL')
        return url


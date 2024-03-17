from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def webdriver_wait_by_name(driver, time, locator):
    wait = WebDriverWait(driver, time).until(expected_conditions.presence_of_element_located((By.NAME, locator)))
    return wait


def webdriver_wait_by_xpath(driver, time, locator):
    wait = WebDriverWait(driver, time).until(expected_conditions.presence_of_element_located((By.XPATH, locator)))
    return wait


def locate_by_name(driver, locator):
    locator = driver.find_element(By.NAME, locator)
    return locator


# def locate_by_id(driver, locator):
#     locator = driver.find_element(By.ID, locator)
#     return locator

def locate_by_xpath(driver, locator):
    locator = driver.find_element(By.XPATH, locator)
    return locator

# def locate_by_class(driver, locator):
#     locator = driver.find_element(By.CLASS_NAME, locator)
#     return locator

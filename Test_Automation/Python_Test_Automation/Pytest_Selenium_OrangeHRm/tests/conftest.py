import pytest
from selenium import webdriver

from utilities.read_config import ReadConfig


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        screenshot_name = f".\\screenshots\\{item.name}.png"
        driver.execute_script("return document.body.scrollHeight")
        driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved as {screenshot_name}")


@pytest.fixture(autouse=True, scope="class")
def setup_teardown(request):
    global driver
    if ReadConfig.get_browser() == "chrome":
        driver = webdriver.Chrome()
    elif ReadConfig.get_browser() == "edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver

# @pytest.hookimpl
# def pytest_runtest_logstart(nodeid):
#     customlogs.get_logs().info(f"started {nodeid}")
#
#
# @pytest.hookimpl
# def pytest_runtest_logfinish(nodeid):
#     customlogs.get_logs().info(f"ended {nodeid}")

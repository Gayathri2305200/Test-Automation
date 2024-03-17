
import pytest
from selenium import webdriver
from utilities.read_cofigurations import ReadConfig

browsers = ReadConfig.get_browsers()


@pytest.fixture(scope="class", params=[browsers[0], browsers[1]])
def setup(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    yield driver



# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     rep = outcome.get_result()
#     print(item.funcargs)
#     driver=item.funcargs.get("setup")
#     if rep.failed:
#         screenshot_name = f".\\screenshots\\{item.name}.png"
#         driver.save_screenshot(screenshot_name)
#         print(f"Screenshot saved as {screenshot_name}")



#print(ReadConfig.get_browser())
    # if ReadConfig.get_browser() == "chrome":
    #     driver = webdriver.Chrome()
    # elif ReadConfig.get_browser() == "edge":
    #     driver = webdriver.Edge()
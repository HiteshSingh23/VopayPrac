from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# Contents of the conftest.py file
def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     dest="browser",
                     default="firefox",
                     help="Browser. Valid options are firefox, ie and chrome")


@pytest.fixture
def browser(request):
    "pytest fixture for browser"
    return request.config.getoption("-B")  # Note how this ties to the newly added command line parameter


def get_webdriver(browser, browser_version, platform, os_version):
    "Run the test in browser stack browser stack flag is 'Y'"
    BROWSERSTACK_URL = 'https://shivanikumari1:UF1LLXarX9cquCRCnjnS@hub-cloud.browserstack.com/wd/hub'
    # USERNAME = shivanikumari1  # We fetch values from a conf file in our framework we use on our clients
    # PASSWORD = accesskey
    desired_capabilities = {}
    if browser.lower() == 'firefox':
        desired_capabilities = DesiredCapabilities.FIREFOX
    if browser.lower() == 'chrome':
        desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities['os'] = platform
    desired_capabilities['os_version'] = os_version
    desired_capabilities['browser_version'] = browser_version

    driver = webdriver.Remote(command_executor=BROWSERSTACK_URL,
                              desired_capabilities=desired_capabilities)

    yield driver
    driver.quit()


"""ios"""

#
# @pytest.fixture(scope='session')
# def browser():
#     BROWSERSTACK_URL = 'https://shivanikumari1:UF1LLXarX9cquCRCnjnS@hub-cloud.browserstack.com/wd/hub'
#
#     """mac desktop"""
#
#     desired_cap = {
#         "os": "OS X",
#         "os_version": "Catalina",
#         "browser": "Safari",
#         "browser_version": "13.0",
#         "browserstack.local": "false",
#         "browserstack.selenium_version": "3.14.0"
#     }
#     """ios device"""
#     # desired_cap={
#     #     'browserName': 'android',
#     #     'device': 'Samsung Galaxy A11',
#     #     'realMobile': 'true',
#     #     'os_version': '10.0',
#     #     'name': "Vopay test"
#     # }
#
#     driver = webdriver.Remote(
#         command_executor=BROWSERSTACK_URL,
#         desired_capabilities=desired_cap
#     )
#
#     yield driver
#     driver.quit()

# """android"""
# @pytest.fixture(scope='session')
# def browser():
#     BROWSERSTACK_URL = 'https://shivanikumari1:UF1LLXarX9cquCRCnjnS@hub-cloud.browserstack.com/wd/hub'
#
#     desired_cap = {
#
#         'browserName': 'android',
#         'device': 'Samsung Galaxy A11',
#         'realMobile': 'true',
#         'os_version': '10.0',
#         'name': "Vopay test"
#
#     }
#
#     driver = webdriver.Remote(
#         command_executor=BROWSERSTACK_URL,
#         desired_capabilities=desired_cap
#     )
#
#     yield driver
#     driver.quit()
#
#

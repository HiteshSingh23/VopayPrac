"""
This module contains shared fixtures for web UI tests.
For now, only Chrome browser is supported.
"""

import json
from lib2to3.pgen2 import driver

import pytest
import allure
import os

from allure_commons.types import AttachmentType
from selenium.webdriver import Firefox
from selenium.webdriver.firefox import options
from selenium.webdriver.chrome.options import Options



# CONFIG_PATH = 'resources\config.json'
# CONFIG_PATH = os.getcwd() + r'\\resources\\config.json'
CONFIG_PATH = os.getcwd() + "/resources/config.json"
Browser_path = "/usr/local/bin/geckodriver"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['firefox']

@allure.step('Reading config from json file')
@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data

@allure.step('Configuring browser')
@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    # To extend the browser support in future
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    # elif config['browser'] not in SUPPORTED_BROWSERS:
    #     raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']

@allure.step('Configuring the wait time for browser')
@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' or rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:  # assume this is fixture with webdriver
                    web_driver = item.funcargs['browser']
                # else :
                #     print('Fail to take screen-shot')
                #     return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))

@allure.step('Initializing the configured browser')
@pytest.fixture(scope='session')
def browser(config_browser, config_wait_time, request):
    # Initialize WebDriver
    if config_browser == 'firefox':
        options = Options()
        options.add_argument('log-level=3')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"')
        # chrome_options.add_argument("--window-size=1920x1080")  # options=options
        driver = Firefox(Browser_path, options=options)
        # else:
        #     raise Exception(f'"{config_browser}" is not a supported browser')

        # Wait implicitly for elements to be ready before attempting interactions
        driver.implicitly_wait(config_wait_time)
        driver.maximize_window()

        # Return the driver object at the end of setup
        yield driver

        # For cleanup, quit the driver
        driver.quit()
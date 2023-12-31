import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from shop_book.utils import attach
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()



@pytest.fixture(scope='function', autouse=True)
def driver_managment_remote():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options)

    browser.config.driver = driver
    browser.config.window_width = 1200
    browser.config.window_height = 800

    yield browser
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()

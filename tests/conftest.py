import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.base_url = 'https://github.com'
    browser.driver.set_window_size(width=1920, height=1080)
    driver_options = webdriver.ChromeOptions()
    browser.config.driver_options = driver_options
    browser.config.timeout = 2

    yield

    browser.quit()

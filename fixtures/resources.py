from time import time

import pytest
from selenium import webdriver
import platform

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def is_mac():
    return f"{platform.mac_ver()[0]}".strip() != ''


@pytest.fixture(scope="function")
def seleniumdriver(is_mac):

    if is_mac:
        s = Service('./mac/chromedriver')
    else:
        s = Service('./windows/chromedriver.exe')

    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture(scope="function")
def wait_for_invisibility(seleniumdriver):
    def _do_wait(element, time_to_wait = 10):
        start_time = time()
        while start_time + time_to_wait > time():
            try:
                element.is_displayed()
            except StaleElementReferenceException as Exception:
                return
        assert False, "Timeout waiting for element to disappear"

    yield _do_wait

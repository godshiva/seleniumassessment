import pytest
from selenium import webdriver
import platform
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


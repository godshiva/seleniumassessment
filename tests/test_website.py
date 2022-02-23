import time

import pytest
import requests as requests
from selenium.webdriver.common.by import By


def test_broken_images(seleniumdriver):
    seleniumdriver.get("http://the-internet.herokuapp.com/broken_images")
    invalid_files = []
    for tag in seleniumdriver.find_elements(By.TAG_NAME, "img"):
        source_file = f"{tag.get_attribute('src')}"
        response = requests.get(source_file, stream=True).status_code
        print(response)
        if response != 200:
            invalid_files.append(source_file)

    # 'normal' test to raise a flag if an image is missing
    # assert len(invalid_files) == 0, " ".join(invalid_files) + " missing from page"

    # 'special' test to demonstrate coder can determine what images are missing
    assert invalid_files == ['http://the-internet.herokuapp.com/asdf.jpg', 'http://the-internet.herokuapp.com/hjkl.jpg'], " ".join(invalid_files) + " missing from page"


def test_select_from_dropdown(seleniumdriver):
    seleniumdriver.get("http://the-internet.herokuapp.com/dropdown")

    assert True

def test_notification_message(seleniumdriver):
    seleniumdriver.get("http://the-internet.herokuapp.com/notification_message")

    assert True

def test_click_button_dismiss_alert(seleniumdriver):
    seleniumdriver.get("http://the-internet.herokuapp.com/javascript_alerts")

    assert True

def test_detect_typo(seleniumdriver):
    seleniumdriver.get("http://the-internet.herokuapp.com/typos")

    assert True

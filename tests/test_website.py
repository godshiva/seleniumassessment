import time

import pytest
import requests as requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.skip("hold on")
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


@pytest.mark.skip("hold on")
def test_select_from_dropdown(seleniumdriver):
    seleniumdriver.get("http://the-internet.herokuapp.com/dropdown")
    select_object = Select(seleniumdriver.find_element(By.CSS_SELECTOR, "#dropdown"));
    select_object.select_by_value("1")
    time.sleep(3)
    elements = seleniumdriver.find_elements(By.TAG_NAME, "select>option[selected='selected']")
    assert len(elements) == 1 and elements[0].get_attribute('value') == '1', f"Invalid selection {elements}"


@pytest.mark.skip("hold on")
def test_notification_message(seleniumdriver, wait_for_invisibility):
    seleniumdriver.get("http://the-internet.herokuapp.com/notification_message")

    # see if existing notification message exists, if so, close it

    elements = seleniumdriver.find_elements(By.CSS_SELECTOR, "a.close")
    assert len(elements) < 2, f"Unexpected configuration {elements}"
    if len(elements) == 1:
        elements[0].click()
        wait_for_invisibility(elements[0])

    assert len(seleniumdriver.find_elements(By.CSS_SELECTOR, "#flash")) == 0

    seleniumdriver.find_element(By.CSS_SELECTOR, "a[href*='notification_message']").click()

    element = seleniumdriver.find_element(By.CSS_SELECTOR, "#flash")
    assert 'Action' in element.text, f"Unexpected text from message {element}"


@pytest.mark.skip("hold on")
def test_click_button_dismiss_alert(seleniumdriver):
    seleniumdriver.get("http://the-internet.herokuapp.com/javascript_alerts")



@pytest.mark.skip("hold on")
def test_detect_typo(seleniumdriver):
    seleniumdriver.get("http://the-internet.herokuapp.com/typos")


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
def test_notification_message(seleniumdriver):
    seleniumdriver.get("http://the-internet.herokuapp.com/notification_message")



@pytest.mark.skip("hold on")
def test_click_button_dismiss_alert(seleniumdriver):
    seleniumdriver.get("http://the-internet.herokuapp.com/javascript_alerts")



@pytest.mark.skip("hold on")
def test_detect_typo(seleniumdriver):
    seleniumdriver.get("http://the-internet.herokuapp.com/typos")


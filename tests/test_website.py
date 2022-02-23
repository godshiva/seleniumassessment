import time

import pytest



def test_yahoo(seleniumdriver):
    seleniumdriver.get("https://www.yahoo.com/")
    time.sleep(3)
    assert True


def test_google(seleniumdriver):
    seleniumdriver.get("https://www.google.com/")
    time.sleep(3)
    assert True
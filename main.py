import os
import time
from selenium import webdriver
import platform

from selenium.webdriver.chrome.service import Service

if f"{platform.mac_ver()[0]}".strip() == '':
    # we're on windows!
    s = Service('./windows/chromedriver.exe')
else:
    # we're on a mac!
    s = Service('./mac/chromedriver')

driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/")
driver.refresh()
driver.close()

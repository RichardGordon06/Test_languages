from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

try:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser=webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    assert button, "No button"
finally:
    time.sleep(3)
    browser.quit()
        


import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_bascket(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, '[value="Добавить в корзину"]')
    assert len(button) > 0, "Element wasn't found"
    time.sleep(10)
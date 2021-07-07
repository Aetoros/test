import pytest
from selenium import webdriver
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_add_to_basket_button(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    button = browser.find_element_by_css_selector("#add_to_basket_form button")
    assert button is not None, "Button not found"
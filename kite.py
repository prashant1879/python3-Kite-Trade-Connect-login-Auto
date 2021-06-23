#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from urlparse import urlparse, parse_qs
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
timout = 5
display = Display(visible=0, size=(1024, 768))
display.start()
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://kite.trade/connect/login?v=3&api_key=API_KEY")
username = driver.find_element_by_xpath("//input[@id='userid']")
password = driver.find_element_by_xpath("//input[@id='password']")
username.send_keys("USERiD")
password.send_keys("PASSwORD")
driver.find_element_by_tag_name('button').click()
driver.implicitly_wait(10)
pin = driver.find_element_by_xpath("//input[@id='pin']")
pin.send_keys("PiN")
driver.find_element_by_tag_name('button').click()
driver.implicitly_wait(10)
driver.get_screenshot_as_file("capture.png")
driver.close()

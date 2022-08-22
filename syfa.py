from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
import names
import secrets
import random
import string
import os


driver = webdriver.Chrome()
time.sleep(t2)
driver.get(url)
time.sleep(t)
driver.find_element_by_xpath('//*[@id="HTML7"]/div[1]/button').click()
time.sleep(10)
driver.find_element_by_xpath('//*[@id="iframeDisplay"]').click()
time.sleep(w)
driver.switch_to.window(driver.window_handles[0])
time.sleep(t1)

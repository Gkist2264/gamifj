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


url_list= ['https://shortznewz.blogspot.com/2022/04/some-best-places-in-dubai.html?m=1', 'https://shortznewz.blogspot.com/2022/04/best-places-to-visit.html', 'https://shortznewz.blogspot.com/2022/04/facts-about-humans.html', 'https://shortznewz.blogspot.com/2022/04/random-facts.html', 'https://shortznewz.blogspot.com/2022/04/interesting-facts.html']
url = random.choice(url_list)

w = random.randint(33,75)
t = random.randint(10,25)
t1 = random.randint(138,50)
t2 = random.randint(5,40)

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

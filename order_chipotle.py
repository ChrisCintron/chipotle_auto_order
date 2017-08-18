

#Author
"""
Author: Christopher Cintron
"""
#Description
"""
Selenium script that logs into banking website
and retrieves banking information
"""




#__Start_script__#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from user_data import *


driver = webdriver.Chrome()
driver.get(url)



driver.find_element_by_id('headerGreeting').click()
driver.find_element_by_id('email').send_keys(info['Chris']['email'])
driver.find_element_by_id('password-input').send_keys(info['Chris']['password'])
driver.find_element_by_id('sign-in').click()
time.sleep(1)
driver.find_element_by_name("BURRITO BOWL").click()
time.sleep(1)

def pick_menu(menu, specific_order):
    for ingredients in specific_order:
        time.sleep(1)
        driver.find_element_by_id(menu[ingredients]).click()


def checkout():
    driver.find_element_by_xpath('//*[@id="elevator"]/div[3]/cmg-arrow-button').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="bag-container"]/div[5]/div[2]/button[2]').click()
    time.sleep(1)
    driver.find_element_by_class_name('btn-checkout-continue').click()
    time.sleep(1)
    #pickup_time = driver.find_element_by_name('select name').text
    #print(pickup_time)



pick_menu(menu, info['Chris']['order'])
checkout()



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


def login():
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
    #Add to bags continue
    driver.find_element_by_xpath('//*[@id="elevator"]/div[3]/cmg-arrow-button').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="bag-container"]/div[5]/div[2]/button[2]').click()
    time.sleep(1)
    #Pickup Restaurant
    driver.find_element_by_class_name('btn-checkout-continue').click()
    time.sleep(1)
    #Pickup Time
    pickup_time = driver.find_element_by_name('select name').text[0:4]
    driver.find_element_by_class_name('btn-checkout-continue').click()
    time.sleep(1)
    #Payment
    driver.find_element_by_class_name('btn-checkout-continue').click()
    time.sleep(1)
    #Submit button
    #This line is hashed for testing
    #driver.find_element_by_id('submit-order').click()
    print('Pickup-Time: ' + pickup_time)



if __name__ == '__main__':
    login()
    pick_menu(menu, info['Chris']['order'])
    checkout()

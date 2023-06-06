import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class Multiple_products_in_RFQ():

    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver.exe")

    driver.maximize_window()

    # Code for zooming out to 80%
    # driver.execute_script("document.body.style.zoom='80%'")
    
    PATH= "http://beta.blitznet.co.id/signin"
    
    # 1 | Go to the entered link/website.
    driver.get(PATH)

    # driver.fullscreen_window()

    # 2 | click | id=email | 
    driver.find_element(By.ID, "email").click()
    # 3 | type | id=email | vijaychauhan@yopmail.com
    driver.find_element(By.ID, "email").send_keys("vijaychauhan@yopmail.com")
    # 4 | type | id=password | vijaychauhan@yopmail.com
    driver.find_element(By.ID, "password").send_keys("vijaychauhan@yopmail.com")
    # 5 | click | id=buyerLoginInBtnId | 
    driver.find_element(By.ID, "buyerLoginInBtnId").click()
    # 6 | pause | 5000 | 
    time.sleep(8)
    # 7 | click | css=.col-md-12 > #filldetailsmodal | 
    close_popup = driver.find_element(By.CSS_SELECTOR, ".col-md-12 > #filldetailsmodal").click()
    # 8 | pause | 5000 | 
    time.sleep(2)

    # Number of products need to be added.
    num_of_products = int(input("How many products you need to add: "))
    
    for i in range(num_of_products):
        # 9 | click | id=tags | 
        search_product = driver.find_element(By.ID, "tags").click()
        # 10 | type | id=tags | ola
        search_product = driver.find_element(By.ID, "tags").send_keys("ola")
        time.sleep(2)
        # 11 | click | id=ui-id-3 | 
        search_product = driver.find_element(By.XPATH,"/html/body/ul/li[1]/div").click()
        time.sleep(2)
        # 12 | click | id=quantity | 
        search_product = driver.find_element(By.ID, "quantity").click()
        # 13 | type | id=quantity | 50
        search_product =  driver.find_element(By.ID, "quantity").send_keys("50")
        # 14 | click | id=unit | 
        search_product = driver.find_element(By.ID, "unit").click()
        # 15 | select | id=unit | label=Roll
        # dropdown = driver.find_element(By.ID, "unit")
        dropdown = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/div[2]/div/form/div[3]/div[1]/div/div[6]/select/option[2]").click()
        # 16 | click | id=product_description | 
        add_product = driver.find_element(By.ID, "product_description").click()
        # 17 | type | id=product_description | Automation
        add_product = driver.find_element(By.ID, "product_description").send_keys("Automation Testing")
        # 18 | click | id=add_product_btn | 
        add_product = driver.find_element(By.ID, "add_product_btn").click()
        time.sleep(2)
    
    time.sleep(5)

    driver.quit()
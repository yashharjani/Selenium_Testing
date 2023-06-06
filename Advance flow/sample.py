import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class get_order_number():

    driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver.exe")
    driver.maximize_window()
    PATH= "http://beta.blitznet.co.id/signin"
    # Go to the entered link/website.
    driver.get(PATH)
    # Login as a Buyer.
    driver.find_element(By.ID, "email").click()
    driver.find_element(By.ID, "email").send_keys("vijaychauhan@yopmail.com")
    driver.find_element(By.ID, "password").send_keys("vijaychauhan@yopmail.com")
    driver.find_element(By.ID, "buyerLoginInBtnId").click()
    time.sleep(6)
    # Close the company details percentage pop-up
    close_popup = driver.find_element(By.CSS_SELECTOR, ".col-md-12 > #filldetailsmodal").click()
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0,500)")
    time.sleep(0.5)
    open_orders_tab = driver.find_element(By.XPATH,"//*[@id='userinfo']/div[2]/div/div/div[3]/a").click()
    time.sleep(1)
    # get_order_no = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/div[2]/input[1]").get_attribute("value")

    get_order_no = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/div[2]/input[1]").get_attribute("value")
    # time.sleep(1)

    print(get_order_no)

    driver.quit()

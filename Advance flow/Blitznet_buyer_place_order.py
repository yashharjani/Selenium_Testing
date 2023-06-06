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
from admin import rfq_no

class Blitznet_buyer_place_order:

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
    time.sleep(1)

    # Open RFQs tab.
    # open_rfqs_tab = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[2]/a").click()
    # time.sleep(1)

    open_rfqs_tab =driver.find_element(By.ID,"myRfqCount").click()

    # Open recent RFQ response received by dropdown.
    # open_rfq_response_received = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/div[2]/div[1]/h2/button").click()
    # time.sleep(3)
    # open_rfq_response_received = driver.find_element(By.CSS_SELECTOR,"button[data-id='5353']").click()
    # time.sleep(3)
    rfq_no2 = rfq_no
    open_rfq_response_received = driver.find_element(By.CSS_SELECTOR,"button[data-id='"+rfq_no2+"']").click()
    time.sleep(0.5)

    driver.execute_script("window.scrollTo(0,400)")
    time.sleep(0.5)

    open_rfq_response_received = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/div[2]/div[1]/div/div/div[3]/div/div/h2/button").click()
    time.sleep(0.5)

    # Place order.
    place_order = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div[2]/div/a").click()
    time.sleep(1)

    # place_order = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[7]/div/div/form/div[2]/div[4]/button").click()
    place_order = driver.find_element(By.ID,"placeOrderBtn").click()
    time.sleep(1)

    # customer_reference_id = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[9]/div/div/div[2]/button[1]").click()
    customer_reference_id = driver.find_element(By.ID,"orderPlaceBtn").click()
    time.sleep(1)

    # open_orders = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[2]/div/div/div[3]/a").click()
    # time.sleep(2)

    driver.quit()
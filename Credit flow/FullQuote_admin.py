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

class Send_FullQuote_Admin():

    # Launching the chrome browser.
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver.exe")

    driver.maximize_window()

    PATH= "https://beta.blitznet.co.id/admin/login"

    # Go to the entered link/website.
    driver.get(PATH)

    # Code for zooming out to 80%
    # driver.execute_script("document.body.style.zoom='80%'")

    # Login as an admin
    username = driver.find_element(By.ID,"email")
    username.send_keys("admin@blitznet.com")

    password = driver.find_element(By.ID,"password")
    password.send_keys("admin@123")

    submit = driver.find_element(By.ID,"supplierLogInBtn")
    submit.send_keys(Keys.RETURN)

    time.sleep(0.5)

    #Open RFQs tab in admin side. 
    open_rfq_tab = driver.find_element(By.XPATH,"/html/body/div[1]/div/nav/ul/li[7]/a/span").click()
    time.sleep(0.5)
    open_rfq_tab = driver.find_element(By.XPATH,"/html/body/div[1]/div/nav/ul/li[7]/div/ul/li[1]/a/span[1]").click()
    time.sleep(0.5)

    #Open the recent RFQ by clicking on Edit button.
    edit_rfq = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[3]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[10]/a[3]").click()

    time.sleep(1)

    # driver.execute_script("window.scrollTo(0,1000)")
    # Click on send quotes button.
    send_quote = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div[3]/a[2]").click()

    time.sleep(1)

    driver.execute_script("window.scrollTo(0,400)")

    time.sleep(0.5)

    # Select supplier from dropdown or by search.
    select_supplier = driver.find_element(By.ID,"select2-supplier-container").click()

    # time.sleep(1)

    type_select_supplier = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input").send_keys("John")
    type_select_supplier = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)

    time.sleep(1)

    # Select product checkbox and fill in the relavant details.
    product_checkbox = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[2]/div/div[2]/div/div/div[1]/h2/div/input[1]").click()

    # time.sleep(1)

    product_checkbox = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[2]/div/div[2]/div/div/div[1]/h2/button").click()

    # time.sleep(1)

    driver.execute_script("window.scrollTo(0,700)")

    time.sleep(0.5)
    
    enter_product_details = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/input[1]").send_keys("10")

    enter_product_details = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/input").send_keys("1000")

    time.sleep(1)

    driver.execute_script("window.scrollTo(0,850)")
    time.sleep(0.5)

    # Fill the address details.
    fill_address = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[3]/div/div[2]/div/div[1]/span/span[1]/span").click()

    # time.sleep(1)

    # fill_address = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[3]/div/div[2]/div/div[1]/select/option[2]").click()

    fill_address = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input").send_keys("Indonesian")
    fill_address = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input").send_keys(Keys.RETURN)

    time.sleep(1)

    driver.execute_script("window.scrollTo(0,1400)")
    time.sleep(1)

    # Fill in supplier other charges and its relavant details.
    logistic_checkbox = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[4]/div/div[1]/h5/div[2]/span[1]/input").click()
    time.sleep(0.5)

    supplier_other_charges = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[4]/div/div[2]/div/div[1]/div[2]/select").click()
    time.sleep(0.5)

    supplier_other_charges = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[4]/div/div[2]/div/div[1]/div[2]/select/option[3]").click()

    time.sleep(0.5)

    driver.execute_script("window.scrollTo(0,1950)")
    time.sleep(0.5)

    # Fill in other details.
    other_delivery_details = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[7]/div/div[2]/div/div[1]/input").send_keys("Delivery will be on time !")

    other_delivery_details = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[7]/div/div[2]/div/div[3]/input").send_keys("3")
    
    other_delivery_details = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[7]/div/div[2]/div/div[4]/input").send_keys("10")

    time.sleep(0.5)

    other_delivery_details = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[7]/div/div[2]/div/div[5]/div/input").click()

    # driver.execute_script("window.scrollTo(0,2050)")

    # time.sleep(5)
    
    other_delivery_details = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/table/tbody/tr[5]/td[6]").click()

    time.sleep(0.5)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Give Tax amount and then click on calculate
    tax_value = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[8]/div/div[2]/div/div[1]/input").send_keys(Keys.BACKSPACE)
    
    tax_value = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[8]/div/div[2]/div/div[1]/input").send_keys("10")

    time.sleep(0.5)

    cal_final_amt = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[8]/div/div[2]/div/div[3]/div/button").click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(0.5)

    # If terms and conditions checkbox comes.
    # checkbox = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[10]/div[1]/div[1]/input").click()
    # time.sleep(1)

    # Submit quote.
    submit_quote = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/form/div/div[10]/div/button").click()
    time.sleep(1)

    confirm = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[4]/div[2]/button").click()

    time.sleep(1)

    driver.quit()

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

class Placing_rfq_credit():

    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver.exe")

    # create action chain object
    action = ActionChains(driver)

    driver.maximize_window()
    
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
    time.sleep(6)
    # 7 | click | css=.col-md-12 > #filldetailsmodal | 
    close_popup = driver.find_element(By.CSS_SELECTOR, ".col-md-12 > #filldetailsmodal").click()
    # 8 | pause | 5000 | 
    time.sleep(1)
    # 9 | click | id=tags | 
    search_product = driver.find_element(By.ID, "tags").click()
    # 10 | type | id=tags | ola
    search_product = driver.find_element(By.ID, "tags").send_keys("ola")
    time.sleep(1)
    # 11 | click | id=ui-id-3 | 
    search_product = driver.find_element(By.XPATH,"/html/body/ul/li[1]/div").click()
    time.sleep(1)
    # 12 | click | id=quantity | 
    search_product = driver.find_element(By.ID, "quantity").click()
    # 13 | type | id=quantity | 50
    search_product =  driver.find_element(By.ID, "quantity").send_keys("50")
    # 14 | click | id=unit | 
    search_product = driver.find_element(By.ID, "unit").click()
    # 15 | select | id=unit | label=Roll
    # dropdown = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/div[2]/div/form/div[3]/div[1]/div/div[6]/select").click()
    dropdown = driver.find_element(By.ID,"unit").click()
    # time.sleep(1)
    dropdown = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/div[2]/div/form/div[3]/div[1]/div/div[6]/select/option[3]").click()
    time.sleep(0.5)
    # 16 | click | id=product_description | 
    add_product = driver.find_element(By.ID, "product_description").click()
    # 17 | type | id=product_description | Automation
    add_product = driver.find_element(By.ID, "product_description").send_keys("This RFQ has been placed by Automation test script.")
    # 18 | click | id=add_product_btn | 
    add_product = driver.find_element(By.ID, "add_product_btn").click()

    # # If write a review pop-up appears
    # if driver.find_element(By.XPATH,"/html/body/div[7]/div/div[2]"):
    #     driver.find_element(By.XPATH,"/html/body/div[7]/div/div[3]/div/button").click()
    # time.sleep(1)
    # try:
    #     print('Try find Review pop-up box')
    #     checkup_click_understand = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[3]/div/button')))
    #     checkup_click_understand.click()
    #     # if checkup_click_understand.size > 0:
    #     #     actions = webdriver.ActionChains(driver)
    #     #     actions.click(checkup_click_understand)
    #     #     actions.perform()
    #     time.sleep(5)
    #     rating_star = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/div[3]/div/div/div/form/div[1]/div[1]/div[3]/div")
    #     rating_star_add = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/div[3]/div/div/div/form/div[1]/div[1]/div[3]/div/div[3]/span[1]").click()
    #     time.sleep(10)
    # except TimeoutException:
    #     print('No Review Pop-up box')

    # 19 | runScript | window.scrollTo(0,500) | 
    driver.execute_script("window.scrollTo(0,500)")
    # 24 | pause | 3000 | 
    time.sleep(1)
    # 25 | runScript | window.scrollTo(0,666.25) | 
    driver.execute_script("window.scrollTo(0,666.25)")
    # 26 | click | id=expected_date | 
    driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/div[2]/div/form/div[20]/input").click()
    # 27 | click | linkText=24 | 
    driver.find_element(By.LINK_TEXT, "15").click()
    time.sleep(1)
    # 28 | click | css=.form-check-inline:nth-child(2) > .form-check-label | 
    # driver.find_element(By.CSS_SELECTOR, ".form-check-inline:nth-child(2) > .form-check-label").click()
    driver.execute_script("window.scrollTo(0,1000)")
    time.sleep(1)

    # credit box
    credit_select = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/div[2]/div/form/div[28]/div/div[1]/div/input").click()
    time.sleep(0.5)
    credit_select = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/div[2]/div/form/div[28]/div/div[2]/select").click()
    time.sleep(0.5)
    credit_select = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/div[2]/div/form/div[28]/div/div[2]/select/option[4]").click()
    time.sleep(1)


    preferred_supplier = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/div[2]/div/form/div[29]/div/div[1]/div[2]/input").click()
    time.sleep(1)
    
    # 31 | click | id=submitQuickRfqPost | 
    driver.find_element(By.ID, "submitQuickRfqPost").click()
    # 32 | pause | 5000 | 
    time.sleep(1)
  
    driver.quit()
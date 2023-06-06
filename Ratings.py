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

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver.exe")

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
time.sleep(8)
# 7 | click | css=.col-md-12 > #filldetailsmodal | 
close_popup = driver.find_element(By.CSS_SELECTOR, ".col-md-12 > #filldetailsmodal").click()
# 8 | pause | 5000 | 
time.sleep(1)

add_product = driver.find_element(By.ID, "add_product_btn").click()
time.sleep(1)

rating_popup = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[3]/div/button").click()
time.sleep(1)

add_stars = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/div[6]/div/div/div/form/div[1]/div[1]/div[3]/div/div[4]/span[1]").click()
time.sleep(3)
# add_stars = driver.find_element(By.XPATH,"//*[@id='addReviewform']/div[1]/div[1]/div[3]/div/div[4]/span[2]").click()
time.sleep(5)

driver.quit()
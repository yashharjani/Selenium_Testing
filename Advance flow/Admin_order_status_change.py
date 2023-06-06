import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver.exe")
driver.maximize_window()
PATH= "http://beta.blitznet.co.id/admin/login"
# Go to the entered link/website.
driver.get(PATH)

# Login as an admin
username = driver.find_element(By.ID,"email")
username.send_keys("admin@blitznet.com")
password = driver.find_element(By.ID,"password")
password.send_keys("admin@123")
submit = driver.find_element(By.ID,"supplierLogInBtn")
submit.send_keys(Keys.RETURN)
time.sleep(3)

# Change language to english
change_lang = driver.find_element(By.XPATH,"/html/body/div[1]/nav/div[2]/ul/li[3]/div/button").click()
time.sleep(1)
change_lang = driver.find_element(By.XPATH,"/html/body/div[1]/nav/div[2]/ul/li[3]/div/ul/li[2]/a").click()
time.sleep(2)

# Open orders tab.
open_orders = driver.find_element(By.XPATH,"/html/body/div[1]/div/nav/ul/li[9]/a").click()
time.sleep(1)
open_orders = driver.find_element(By.XPATH,"/html/body/div[1]/div/nav/ul/li[9]/div/ul/li[1]/a").click()
time.sleep(5)

# open_edit_order = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[12]/a[1]").click()

open_edit_order = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[12]/a[1]").click()


time.sleep(3)

# Change status from order placed to order confirmed and payement pending.
change_status = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div/select").click()
time.sleep(1)

change_status = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div/select/option[2]").click()
time.sleep(1)
change_status = driver.find_element(By.XPATH,"/html/body/div[8]/div/div[4]/div[2]/button").click()
time.sleep(3)

# Change order status from Order confirmed and payment pending to Payment done.
change_status = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div/select").click()
time.sleep(1)
change_status = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div/select/option[3]").click()
time.sleep(2)
change_status = driver.find_element(By.XPATH,"/html/body/div[8]/div/div[4]/div[2]/button").click()
time.sleep(3)

driver.execute_script("window.scrollTo(0,850)")
time.sleep(2)

# Change order item status from under preparation (up) to Ready to dispatch (rtd).
up_to_rtd = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[3]/div/div[2]/div[4]/div[1]/div/select").click()
time.sleep(1)
up_to_rtd = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[3]/div/div[2]/div[4]/div[1]/div/select/option[2]").click()
time.sleep(2)
# confirm pop-up
up_to_rtd = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[3]/div/div[2]/div[7]/div/div/div[3]/div[2]/button").click()
time.sleep(2)
# Select date and time.
up_to_rtd = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[3]/div/div[2]/div[3]/div/form/div/div[2]/div[1]/input").click()
time.sleep(1)
up_to_rtd = driver.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div[2]/div/span[35]").click()
time.sleep(1)
up_to_rtd = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[3]/div/div[2]/div[3]/div/form/div/div[3]/button[2]").click()
time.sleep(3)

# Change status from Ready to dispatch (rtd) to Order pickup (op)
rtd_to_op = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[3]/div/form/span/label").send_keys("C:/vscode selenium practice/dummy3.jpg")

driver.quit()
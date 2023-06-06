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

driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver.exe")
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)
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
time.sleep(1)

open_quotes = driver.find_element(By.XPATH,"/html/body/div[1]/div/nav/ul/li[8]/a").click()

time.sleep(3)

# buyer_comp_name = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[5]").get_attribute("innerHTML")

# if buyer_comp_name == "Automation testing academy":

#     rfq_no = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[3]/a").get_attribute("data-id")
#     print(rfq_no)

# else:
#     print("The buyer company name is not Automation testing academy.")
# # print("Buyer company name: " +buyer_comp_name)

# time.sleep(2)


# table_elements = []
# rows1 = len(driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td"))
# rows2 = len(driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr[1]"))

# print(rows2)

for r in range(1,15):
    # value = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text

    buyer_comp_name = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr["+str(r)+"]/td[5]").get_attribute("innerHTML")

    if buyer_comp_name == "Automation testing academy":

        rfq_no = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr["+str(r)+"]/td[3]/a").get_attribute("data-id")
        print(rfq_no)
        break

driver.quit()
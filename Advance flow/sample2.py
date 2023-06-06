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

def edit_orders(r):

    edit_orders = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr["+str(r)+"]/td[12]/a[1]").click()
    time.sleep(0.5)

    # # Change status from order placed to order confirmed and payement pending.
    # change_status = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div/select").click()
    # time.sleep(0.5)

    # change_status = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div/select/option[2]").click()
    # time.sleep(1)
    # change_status = driver.find_element(By.XPATH,"/html/body/div[8]/div/div[4]/div[2]/button").click()
    # time.sleep(2)

    # # Change order status from Order confirmed and payment pending to Payment done.
    # change_status = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div/select").click()
    # time.sleep(0.5)
    # change_status = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div/select/option[3]").click()
    # time.sleep(1)
    # change_status = driver.find_element(By.XPATH,"/html/body/div[8]/div/div[4]/div[2]/button").click()
    # time.sleep(2)

    driver.execute_script("window.scrollTo(0,850)")
    time.sleep(1)

    # # Change order item status from under preparation (up) to Ready to dispatch (rtd).
    # up_to_rtd = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[3]/div/div[2]/div[4]/div[1]/div/select").click()
    # time.sleep(0.5)
    # up_to_rtd = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[3]/div/div[2]/div[4]/div[1]/div/select/option[2]").click()
    # time.sleep(1)
    # # confirm pop-up
    # up_to_rtd = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[3]/div/div[2]/div[7]/div/div/div[3]/div[2]/button").click()
    # time.sleep(2)
    # # Select date and time.
    # up_to_rtd = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[3]/div/div[2]/div[3]/div/form/div/div[2]/div[1]/input").click()
    # time.sleep(1)
    # up_to_rtd = driver.find_element(By.XPATH,"/html/body/div[7]/div[2]/div/div[2]/div/span[42]").click()
    # time.sleep(1)
    # up_to_rtd = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[3]/div/div[2]/div[3]/div/form/div/div[3]/button[2]").click()
    # time.sleep(1)

    # Change status from Ready to dispatch (rtd) to Order pickup (op)
    rtd_to_op = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[3]/div/form/span/input").send_keys("C:\\vscode selenium practice\\dummy3.jpg")
    time.sleep(0.5)
    rtd_to_op = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/select").click()
    time.sleep(0.5)
    rtd_to_op = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/select/option[3]").click()
    time.sleep(1)

    # Change status from Order pickup (op) to In transit (it)
    op_to_it = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/select").click()
    time.sleep(0.5)
    op_to_it = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/select/option[4]").click()
    time.sleep(1)
    op_to_it = driver.find_element(By.XPATH,"/html/body/div[8]/div/div[4]/div[2]/button").click()
    time.sleep(1)

    # Change status from In transit (it) to out of delivery (ofd)
    it_to_ofd = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/select").click()
    time.sleep(0.5)
    it_to_ofd = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/select/option[5]").click()
    time.sleep(1)
    it_to_ofd = driver.find_element(By.XPATH,"/html/body/div[8]/div/div[4]/div[2]/button").click()
    time.sleep(1)

    # Change status from Out of delivery (ofd) to under qc (uq)
    ofd_to_uq = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/select").click()
    time.sleep(0.5)
    ofd_to_uq = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/select/option[6]").click()
    time.sleep(1)
    ofd_to_uq = driver.find_element(By.XPATH,"/html/body/div[8]/div/div[4]/div[2]/button").click()
    time.sleep(1)

    # Change status from Under QC (uq) to QC passes (qp)
    uq_to_qp = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/select").click()
    time.sleep(0.5)
    it_to_ofd = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/select/option[8]").click()
    time.sleep(1)
    it_to_ofd = driver.find_element(By.XPATH,"/html/body/div[8]/div/div[4]/div[2]/button").click()
    time.sleep(1)
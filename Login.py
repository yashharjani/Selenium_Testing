from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launching the chrome browser.
class Login():
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver.exe")
    PATH= "http://beta.blitznet.co.id/signin"

    # Go to the entered link/website.
    driver.get(PATH)

    username = driver.find_element(By.ID,"email")
    username.send_keys("vijaychauhan@yopmail.com")

    password = driver.find_element(By.ID,"password")
    password.send_keys("vijaychauhan@yopmail.com")

    submit = driver.find_element(By.ID,"buyerLoginInBtnId")
    submit.send_keys(Keys.RETURN)

    time.sleep(10)

    close_popup = driver.find_element(By.CSS_SELECTOR,".col-md-12 > #filldetailsmodal").click()
    # close_popup.send_keys(Keys.RETURN)

    time.sleep(5)

    driver.quit()

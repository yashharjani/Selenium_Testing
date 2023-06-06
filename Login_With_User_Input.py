from selenium import webdriver
import selenium
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Login_With_User_Input():
    driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver.exe")
    driver.get("http://beta.blitznet.co.id/signin")

    username = driver.find_element(By.ID,"email")
    username_input = input("Enter username: ")
    username.send_keys(username_input)

    password = driver.find_element(By.ID,"password")
    password_input = input("Enter password: ")
    password.send_keys(password_input)

    submit = driver.find_element(By.ID,"buyerLoginInBtnId")
    submit.send_keys(Keys.RETURN)

    time.sleep(10)

    close_popup = driver.find_element(By.CSS_SELECTOR,".col-md-12 > #filldetailsmodal").click()
    # close_popup.send_keys(Keys.RETURN)

    time.sleep(5)

    driver.quit()

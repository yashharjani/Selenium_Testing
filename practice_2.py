from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launching the chrome browser.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Go to the entered link/website.
driver.get("https://www.techwithtim.net/")

# For searching a text (let's say, Test) in the search box and then click enter.
search = driver.find_element(By.NAME, "s")
search.send_keys("Test")
search.send_keys(Keys.RETURN)

# # For clicking a button with ID
# search = driver.find_element(By.ID, "panel-6-2-0-1").click()

# #For saving a screenshot as a file.
# driver.get_screenshot_as_file("sc.png")

# # To end the program after the specified time (here its 5 secs) after the screenshot is taken.
# time.sleep(5)

try:
    main = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # print(main.text)

    articles = main.find_elements(By.TAG_NAME,"article")
    for article in articles:
        header = article.find_elements(By.CLASS_NAME,"entry-summary")
        print(header.text)

finally:
    driver.quit()

from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

import time

from selenium.webdriver.support.wait import WebDriverWait

while(True):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    #autoprint(os.getcwd())
    path = os.getcwd()
    path = os.path.join(os.getcwd(),'chromedriver.exe')
   # print (path)
    driver = webdriver.Chrome(path, options=chrome_options)
    driver.get("https://rutgers.ca1.qualtrics.com/jfe/form/SV_9zUk4qAXzRUXC05")
    wait = WebDriverWait(driver,99999)
    element = wait.until(EC.visibility_of_element_located((By.ID, 'EndOfSurvey')))
    if(element.is_displayed()):
        print("Element found")
    else:
        print("Element not found")

    time.sleep(5)
    driver.close()


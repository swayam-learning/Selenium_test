#          Test Case
# --------------------------
# Open WebBrowser
# OpenUrl https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# Provide email  admin
# Provide Password  admin123
# Click on login
# close browser

import selenium
import time
from selenium import webdriver
driver = webdriver.Chrome("chromedriver.exe") #driver as paramter

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)
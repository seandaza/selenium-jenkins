from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import smtplib
import pandas as pd
from base64 import encode
from datetime import datetime
from selenium import webdriver
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

import chromedriver_autoinstaller

chromedriver_autoinstaller.install() 

chromeOptions = Options()
#chromeOptions.headless = True
chromeOptions.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/95.0.4638.54 Safari/537.36")
#chromeOptions.add_extension(r'C:\Users\jhand\Buster-Captcha-Solver-for-Humans.crx')

driver = webdriver.Chrome(options=chromeOptions)

now = datetime.now() 
year_month_day = now.strftime("%Y-%m-%d")


url = "https://www.keoworld.com/"


#Navigate to the page
driver.get(url)
driver.maximize_window()

title = driver.find_element(By.XPATH, "//*[@id='comp-kwclfsi1']/h2[1]").text
print(title)






driver.quit()
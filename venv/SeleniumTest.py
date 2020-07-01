import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import tabulate
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')

driver.get("https://techwithtim.net")
print(driver.title)

time.sleep(5)
driver.quit()

#  GOOD VIDEO: https://www.youtube.com/watch?v=b5jt2bhSeXs
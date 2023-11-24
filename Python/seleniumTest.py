#!python3

from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('https://inventwithpython.com')
#try:
elem = browser.find_element(By.NAME,' cover-thumb')
print('Found <%s> element with that class name!' % (elem.tag_name))
#except:
#    print('Was not able to find an element with that name.')

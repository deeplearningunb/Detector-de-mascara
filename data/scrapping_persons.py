from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome('./chromedriver')
driver.get('https://thispersondoesnotexist.com/')


for i in range(0, 400):
    try:
        driver.find_element_by_xpath('//*[@id="face"]').screenshot('/home/matheus/Documents/Study/Data science/detect_glasses/nomask/personnotexist'+str(i+100)+').png')
        driver.refresh()
    except:
        pass

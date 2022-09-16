#Job appliaction automation using selenium web driver
#It uses LinkedIn job search platform
#IMPORTING LIBRARIES
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common import keys
import time 

email=YOUR EMAIL
pas=LINKEDIN_PASSWORD
job=LINKEDIN_PASSWORD
PHONE=YOUR PHONE 

options=webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
DRIVER_PATH='./chromedriver.exe'
driver=webdriver.Chrome(executable_path=DRIVER_PATH,options=options )
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3271792941&f_AL=true&f_E=2%2C4&geoId=100506914&keywords=python%20developer&location=Europe&refresh=true')
#SIGNING IN
signin=driver.find_element(By.LINK_TEXT,'Sign in')
signin.click()

username=driver.find_element(By.CSS_SELECTOR, '#username')
username.send_keys(email)

password=driver.find_element(By.CSS_SELECTOR,'#password')
password.send_keys(pas)

signin=driver.find_element(By.CSS_SELECTOR,'.login__form_action_container button')
signin.click()

text='Python Developer'
appl=driver.find_element(By.PARTIAL_LINK_TEXT,text)

appl.click()

Epply=driver.find_element(By.CSS_SELECTOR,'.jobs-s-apply button')
Epply.click()

time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

#Submit the application
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()

time.sleep(5)



driver.close()
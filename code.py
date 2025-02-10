import random
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#initialize webdriver
driver=webdriver.Chrome()

#Open URL and maximize window
driver.get('https://www.lavieworld.com/')
driver.maximize_window()
time.sleep(10)

#scroll home-page
for i in range(0,3):
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
for i in range(0,3):
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
    time.sleep(1)

#later button
later=driver.find_element('xpath','//*[@id="onesignal-slidedown-cancel-button"]')
later.click()
time.sleep(5)

#account
account=driver.find_element('xpath','//*[@id="site-control"]/div[2]/div[2]/a[1]')
account.click()
time.sleep(2)

#email
email=driver.find_element('xpath','//*[@id="customer_email"]')
email.send_keys('harshithag2508@gmail.com')
time.sleep(2)
#password
password=driver.find_element('xpath','//*[@id="customer_password"]')
password.send_keys('Harshitha@25')
time.sleep(2)
#sign-in button
sign_in=driver.find_element('xpath','//*[@id="customer_login"]/div[2]/div[3]/input')
sign_in.click()
time.sleep(5)

#new-launches
new_launches=driver.find_element('xpath','//*[@id="site-control"]/div[2]/div[1]/div/div/ul/li[1]/a')
new_launches.click()
time.sleep(2)

#scroll
for i in range(0,3):
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
for i in range(0,3):
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
    time.sleep(2)

#first_bag
bag1=driver.find_element('xpath','//*[@id="usf_container"]/div[2]/div[2]/div[1]/div/a/span')
bag1.click()
time.sleep(4)

for i in range(0,2):
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
for i in range(0,1):
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
    time.sleep(2)

#plus
plus=driver.find_element('xpath','//*[@id="product-form-template--15776323076157__main-7341250215997"]/div[2]/div[1]/a[2]')
plus.click()
time.sleep(2) 

#add-to-cart
add_to_cart=driver.find_element('xpath','//*[@id="product-form-template--15776323076157__main-7341250215997"]/div[2]/button')
add_to_cart.click()
time.sleep(4)

#collections
collections=driver.find_element('xpath','//*[@id="site-control"]/div[2]/div[1]/div/div/ul/li[2]/a')
collections.click()
time.sleep(2)

for i in range(0,3):
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
for i in range(0,3):
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
    time.sleep(2)

#wallet1
wallet1=driver.find_element('xpath','//*[@id="usf_container"]/div[2]/div[2]/div[4]/div/a/span')
wallet1.click()
time.sleep(4)

#plus1
plus1=driver.find_element('xpath','//*[@id="product-form-template--15776323076157__main-7211736498237"]/div[2]/div[1]/a[2]')
plus1.click()
time.sleep(4)

#add-to-cart1
add_to_cart1=driver.find_element('xpath','//*[@id="product-form-template--15776323076157__main-7211736498237"]/div[2]/button')
add_to_cart1.click()
time.sleep(4)

#cart
cart=driver.find_element('xpath','//*[@id="site-control"]/div[2]/div[2]/a[3]')
cart.click()
time.sleep(4)

#checkout
checkout=driver.find_element('xpath','//*[@id="cartform"]/div[2]/input')
checkout.click()
time.sleep(5)
driver.quit()

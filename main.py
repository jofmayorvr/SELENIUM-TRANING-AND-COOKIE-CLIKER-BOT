import time
from traceback import print_tb

from selenium import webdriver
from selenium.webdriver.common.devtools.v154.debugger import step_into
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def is_active(element_price):
    element_price = element_price.text

    if element_price == "":
        element_price = "0"
    else:
        element_price = element_price

    if seperable(element_price," "):
        if element_price.split(" ")[1] == "million":
            element_price = element_price.split(" ")[0] * 1000000
        elif element_price.split(" ")[1] == "billion":
            element_price = element_price.split(" ")[0] * 1000000000
        elif element_price.split(" ")[1] == "trillion":
            element_price = element_price.split(" ")[0] * 1000000000000
    else:
        element_price = element_price.replace(",","")
        return int(element_price)

    element_price = element_price.replace(",","")
    return int(element_price)

def seperable(string,control):
    if control in string:
        return True
    else:
        return False


url = "https://ozh.github.io/cookieclicker/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

time.sleep(3)

language_button = driver.find_element(by=By.XPATH, value='//*[@id="langSelect-EN"]')
language_button.click()

time.sleep(2)

cookie_button = driver.find_element(by=By.XPATH, value='//*[@id="bigCookie"]')

product_0 = driver.find_element(by=By.XPATH, value='//*[@id="product0"]')
product_1 = driver.find_element(by=By.XPATH, value='//*[@id="product1"]')
product_2 = driver.find_element(by=By.XPATH, value='//*[@id="product2"]')
product_3 = driver.find_element(by=By.XPATH, value='//*[@id="product3"]')
product_4 = driver.find_element(by=By.XPATH, value='//*[@id="product4"]')
product_5 = driver.find_element(by=By.XPATH, value='//*[@id="product5"]')
product_6 = driver.find_element(by=By.XPATH, value='//*[@id="product6"]')
product_7 = driver.find_element(by=By.XPATH, value='//*[@id="product7"]')


a = True
while a:
    cookie_button.click()
    current_cookies = driver.find_element(by=By.XPATH, value='//*[@id="cookies"]').text.split()
    current_cookies = int(current_cookies[0])

    upgrades = driver.find_elements(by=By.XPATH, value='//*[@id="upgrades"]')

    product0_price = driver.find_element(by=By.XPATH, value='//*[@id="productPrice0"]')
    product1_price = driver.find_element(by=By.XPATH, value='//*[@id="productPrice1"]')
    product2_price = driver.find_element(by=By.XPATH, value='//*[@id="productPrice2"]')
    product3_price = driver.find_element(by=By.XPATH, value='//*[@id="productPrice3"]')
    product4_price = driver.find_element(by=By.XPATH, value='//*[@id="productPrice4"]')
    product5_price = driver.find_element(by=By.XPATH, value='//*[@id="productPrice5"]')
    product6_price = driver.find_element(by=By.XPATH, value='//*[@id="productPrice6"]')
    product7_price = driver.find_element(by=By.XPATH, value='//*[@id="productPrice7"]')

    if current_cookies >= is_active(product7_price):
        if is_active(product7_price) == 0:
            pass
        else:
            product_7.click()

    if current_cookies >= is_active(product6_price):
        if is_active(product6_price) == 0:
            pass
        else:
            product_6.click()

    if current_cookies >= is_active(product5_price):
        if is_active(product5_price) == 0:
            pass
        else:
            product_5.click()

    if current_cookies >= is_active(product4_price):
        if is_active(product4_price) == 0:
            pass
        else:
            product_4.click()

    if current_cookies >= is_active(product3_price):
        if is_active(product3_price) == 0:
            pass
        else:
            product_3.click()

    if current_cookies >= is_active(product2_price):
        if is_active(product2_price) == 0:
            pass
        else:
            product_2.click()

    if current_cookies >= is_active(product1_price):
        if is_active(product1_price) == 0:
            pass
        else:
            product_1.click()

    if current_cookies >= is_active(product0_price):
        if is_active(product0_price) == 0:
            pass
        else:
            product_0.click()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://appbrewery.github.io/fake-newsletter-signup/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

first_name_input = driver.find_element(By.XPATH,'//*[@id="signup-form"]/input[1]')
first_name_input.send_keys("jofmayor")

last_name_input = driver.find_element(By.XPATH,'//*[@id="signup-form"]/input[2]')
last_name_input.send_keys("namado")

email_input = driver.find_element(By.XPATH,'//*[@id="signup-form"]/input[3]')
email_input.send_keys("qwerqrew@gqwerqwer.com")

button = driver.find_element(By.XPATH,'//*[@id="signup-form"]/button')
button.click()
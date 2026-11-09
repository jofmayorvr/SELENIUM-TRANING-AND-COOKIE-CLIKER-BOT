from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.python.org/"

#keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("class"))

button = driver.find_element(By.ID, "submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)






#only closes single tab
#driver.close()
#closes entire browser
#driver.quit()
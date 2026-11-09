from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.amazon.com.tr/Apple-Kablosuz-Kulakl%C4%B1k-Engelleme-Bluetooth/dp/B0FQF59PPW"

#keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

price_as_whole = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div/div[1]/span[3]/span[2]/span[1]').text
price_as_fraction = driver.find_element(By.XPATH,'//*[@id="corePriceDisplay_desktop_feature_div"]/div/div[1]/span[3]/span[2]/span[2]').text

print(f'the price is {price_as_whole},{price_as_fraction} ')





#only closes single tab
#driver.close()
#closes entire browser
#driver.quit()
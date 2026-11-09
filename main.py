from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.python.org/"

#keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

events = driver.find_elements(By.CSS_SELECTOR,'.event-widget ul a')
dates = driver.find_elements(By.CSS_SELECTOR,'.event-widget ul time')

names=[]
for event in events:
    names.append(event.text)

stripped_dates=[]
for date in dates:
    stripped_dates.append(date.text)

event_dict={}

for n in range(len(names)):
    event_dict[n] = {
        'name':names[n],
        'date':stripped_dates[n],
    }

print(event_dict)

#only closes single tab
#driver.close()
#closes entire browser
#driver.quit()
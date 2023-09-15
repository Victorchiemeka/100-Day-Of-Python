from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
# Navigate to Amazon.com

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
button = driver.find_element(By.ID, "bigCookie")
button.click()

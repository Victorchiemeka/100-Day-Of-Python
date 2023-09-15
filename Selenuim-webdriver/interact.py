from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service_obj = Service(r"C:\Program Files (x86)\chromedriver.exe")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service_obj, options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# # number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# # print(number.text)
# link = driver.find_element(By.LINK_TEXT, "Love Story")
# # link.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")
firstname = driver.find_element(By.XPATH, value="/html/body/form/input[1]")
firstname.send_keys("Victor")


lastname = driver.find_element(By.XPATH, value="/html/body/form/input[2]")
lastname.send_keys("Mmadu")


email = driver.find_element(By.XPATH, value="/html/body/form/input[3]")
email.send_keys("Victoremeka@gmail.com")

button = driver.find_element(By.XPATH, value="/html/body/form/button")
button.click()

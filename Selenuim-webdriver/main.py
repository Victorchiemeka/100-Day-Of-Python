from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
# Navigate to Amazon.com

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service_obj, options=chrome_options)
# driver.get(
#     "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# )

driver.get("https://www.python.org")
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link = driver.find_element(
    By.CSS_SELECTOR, value=".documentation-widget a"
)
print(documentation_link.text)

bug_link = driver.find_element(
    By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a'
)
print(bug_link.text)
driver.quit()

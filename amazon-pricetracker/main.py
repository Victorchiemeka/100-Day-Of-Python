from bs4 import BeautifulSoup
import smtplib
import requests
import ssl

def send_email(sender_email, receiver_email, subject, message, password):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = sender_email
    receiver_email = receiver_email
    password = 
    message = f"""\
    Subject: {subject}

    {message}
    """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

MY_EMAIL = "victorchukwuemeka127@gmail.com"
PASSWORD = "your_email_password"  # Replace with your Gmail password
MAIN_PRICE = 100
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Set user agent and accept-language headers
headers = {
    "User-Agent": "Your User Agent String Here",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

# Find the product title
title = "Amazon price"

# Find the product price
price_element = soup.find(class_="a-offscreen")
if price_element:
    price_text = price_element.get_text()
    without_dollar = price_text.split("$")[1]
    converted_price = float(without_dollar)
else:
    print("Price not found on the page.")
    converted_price = None

message = f"{title} is now ${converted_price}"
subject = "Amazon Price Alert"  # Set your email subject here

if converted_price is not None and converted_price < MAIN_PRICE:
    send_email(MY_EMAIL, MY_EMAIL, subject, message, PASSWORD)

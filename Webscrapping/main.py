from bs4 import BeautifulSoup
import lxml
import requests


response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup =  BeautifulSoup(yc_web_page, "lxml")
article = soup.find(name="span", class_="titleline")
article_text = article.get("href")
vote = soup.find(name="span", class_= "score").getText()

print(article)
print(article_text)
print(vote)


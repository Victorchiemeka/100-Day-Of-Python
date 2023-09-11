import requests
import lxml
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
myweb = response.text

soup = BeautifulSoup(myweb, "lxml")
all_movies =soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
movies_name = [movies.getText() for movies in all_movies]
mymovies = movies_name[::-1]


with open("movies.txt", mode="w") as file:
    for movies in mymovies:
        file.write(f"{movies}\n")

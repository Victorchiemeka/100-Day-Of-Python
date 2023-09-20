#!/usr/bin/python3
import requests
from flask import Flask, render_template, url_for
import random
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    date = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, now=date)


@app.route("/guess/<name>")
def guess(name):
    url = "https://api.genderize.io"
    age = "https://api.agify.io"
    meter = {"name": name}
    params = {"name": name}
    age = requests.get(age, params=meter)
    my_data = age.json()
    my_age = my_data.get("age")

    response = requests.get(url, params=params)
    data = response.json()
    gender = data.get("gender")
    return render_template("home.html", nam=name, gen=gender, user_age=my_age)


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/726b6f6fc6632bacd8b2"
    response = requests.get(blog_url)
    data = response.json()
    return render_template("blogs.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)

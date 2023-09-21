from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    url = "https://api.npoint.io/eb6cd8a5d783f501ee7d"
    response = requests.get(url)
    data = response.json()
    day_date = datetime.now().day
    date = datetime.now().year
    return render_template("index.html", my_date=date, day=day_date, posts=data)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact")
def get_home():
    return render_template("contact.html")


@app.route("/post/<int:num>")
def get_post(num):
    blog_url = " https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    blog_data = response.json()
    requested_post = None
    for data in blog_data:
        if data["id"] == num:
            requested_post = data
    print(data)
    day_date = datetime.now().day
    date = datetime.now().year
    return render_template("post.html", posts=requested_post, day=day_date, year=date)


if __name__ == "__main__":
    app.run(debug=True)

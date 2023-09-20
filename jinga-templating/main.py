from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    blog_url = " https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    blog_data = response.json()
    return render_template("index.html", posts=blog_data)


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
    return render_template("posts.html", posts=requested_post)


if __name__ == "__main__":
    app.run(debug=True)

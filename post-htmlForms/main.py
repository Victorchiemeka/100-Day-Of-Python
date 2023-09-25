from flask import Flask, render_template
from flask import request
import requests
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    name = None
    password = None
    if request.method == "POST":
        name = request.form.get("email")
        password = request.form.get("password")
        print(name, password)
    return render_template("login.html", my_name=name, my_password=password)


if __name__ == "__main__":
    app.run(debug=True)

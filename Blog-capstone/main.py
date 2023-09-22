from flask import Flask, render_template, request
import requests
from datetime import datetime


import smtplib
import ssl


def send_email(sender_email, receiver_email, subject, message, password):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = sender_email
    receiver_email = receiver_email
    password = password
    message = f"""\
    Subject: {subject}\n\n{message}
    """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


# sender_email = "your_email@gmail.com"
# receiver_email = "receiver_email@gmail.com"
# subject = "Test Subject"
# message = "This is a test message."

# # Make sure to enable "less secure apps" or generate an app-specific password in your Gmail settings
# password = "your_password"

# send_email(sender_email, receiver_email, subject, message, password)
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


@app.route("/form-entry", methods=["POST", "GET"])
def receive_data():
    name = None
    my_email = None
    password = None
    if request.method == "POST":
        name = request.form.get("username")
        email = request.form.get("email")
        number = request.form.get("number")
        message = request.form.get("message")
        sender_email = "victorchukwuemeka127@gmail.com"
        receiver_email = "victorchukwuemeka127@gmail.com"
        subject = "Message"
        password
        my_message = (
            f"\nName: {name}\n Email: {email}\n Number:{number}\n Message:{message}"
        )
        send_email(sender_email, receiver_email, subject, my_message, password)
    return render_template("data.html")


if __name__ == "__main__":
    app.run(debug=True)

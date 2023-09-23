from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class MyForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")


app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"  # Replace with your own secret key


@app.route("/myform", methods=["GET", "POST"])
def myform():
    form = MyForm()

    if form.validate_on_submit():
        name = form.name.data
        # Process the form data, e.g., save to a database
        return redirect(url_for("success"))

    return render_template("myform.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

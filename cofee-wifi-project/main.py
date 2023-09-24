from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe_name = StringField("Cafe Name", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    open_time = StringField("Open", validators=[DataRequired()])
    close_time = StringField("Close", validators=[DataRequired()])
    coffee_rating = SelectField(
        "Coffee Rating",
        choices=[("☕" * i, "☕" * i) for i in range(1, 6)],
        validators=[DataRequired()],
    )
    wifi_rating = SelectField(
        "Wifi Rating",
        choices=[("💪" * i, "💪" * i) for i in range(1, 6)],
        validators=[DataRequired()],
    )
    power_rating = SelectField(
        "Power",
        choices=[("🔌" * i, "🔌" * i) for i in range(1, 6)],
        validators=[DataRequired()])
    submit = SubmitField("Submit")

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


cafes = []


@app.route("/add", methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("bro we are here")
        new_cafe = [
            form.cafe_name.data,
            form.location.data,
            form.open_time.data,
            form.close_time.data,
            form.coffee_rating.data,
            form.wifi_rating.data,
            form.power_rating.data,
        ]
        # cafes.append(new_cafe)
        # print(cafes)

        # Write the new cafe data to cafe-data.csv
        with open("cafe-data.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(new_cafe)

        return redirect("/cafes")
    else:
        return render_template("add.html", form=form)

@app.route("/cafes", methods=["GET", "POST"])
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            print(row)  # Print each row to the console
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)

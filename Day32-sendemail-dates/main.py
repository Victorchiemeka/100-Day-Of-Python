import smtplib

my_email = "mmaduvictor30@gmail.com"
password = "dltqbswbruqhifwv"


with smtplib.SMTP("smtp.gmail.com") as connection:

    connection.starttls()

    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="victorchukwuemeka863@yahoo.com",
        msg ="Subject:Hello\n This is the body of my email."
        )

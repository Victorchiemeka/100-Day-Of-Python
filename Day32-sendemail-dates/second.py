import smtplib
import os

my_email = "mmaduvictor@gmail.com"
app_password = "dltqbswbruqhifwv"  # Replace with your app password

# Create an environment variable for the password
os.environ["EMAIL_PASSWORD"] = app_password

try:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()

    # Use the app password from the environment variable
    password = os.getenv("EMAIL_PASSWORD")
    
    if password:
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="victorchukwuemeka127@gmail.com",
            msg="You are gonna be great bro",
        )
        print("Email sent successfully.")
    else:
        print("Email password not found in environment variables.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    connection.close()


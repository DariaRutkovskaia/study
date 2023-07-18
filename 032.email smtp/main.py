import datetime as dt
import random
import smtplib

my_email = "rutkovskiileonid@gmail.com"
password = "kfczavmjooajtwfr"
planned_day = 0


def send_a_quote():
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        motivation_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="leonidus110792@yahoo.com",
                            msg=f"Subject:Quote of the day\n\n"
                                f"{motivation_quote}")


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == planned_day:
    send_a_quote()
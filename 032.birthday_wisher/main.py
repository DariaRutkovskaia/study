##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib

# 4. Send the letter generated in step 3 to that person's email address.
import pandas

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
MY_EMAIL = "rutkovskiileonid@gmail.com"
MY_PASSWORD = "kfczavmjooajtwfr"


def send_letter(name, mail):
    num = random.randint(1, 3)
    with open(f"letter_templates/letter_{num}.txt") as letter:
        bday_letter = letter.read().replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=mail,
                            msg=f"Subject:Happy Birthday, {name}!!!\n\n"
                                f"{bday_letter}")


now = dt.datetime.now()
now_day = now.day
now_month = now.month

bd_data = pandas.read_csv("birthdays.csv")
month = bd_data["month"]
day = bd_data["day"]
for row in range(len(month)):
    if month[row] == now_month and day[row] == now_day:
        bday_name = bd_data["name"][row]
        e_mail = bd_data["email"][row]
        send_letter(bday_name, e_mail)

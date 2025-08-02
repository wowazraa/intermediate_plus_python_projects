from datetime import *
from pandas import *
from smtplib import *
from random import *

EMAIL = "derinazrairem@gmail.com"
PASSWORD = "gujumnpflgpiegjr"

now = datetime.now()
month = now.month
day=now.day

file = read_csv("birthdays.csv")
file_dict = file.to_dict(orient="records")

for birthday in file_dict:
    if birthday["month"] == month and birthday["day"] == day:
        name = birthday["name"]
        email = birthday["email"]

        letter_num = choice([1, 2, 3])
        with open(f"letter_templates/letter_{letter_num}.txt", "r") as file:
            letter_content = file.read()

        final_letter = letter_content.replace("[NAME]", name)


        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=email,
                                msg=f"Subject:HAPPY BIRTHDAY!\n\n{final_letter}")


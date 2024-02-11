from _datetime import datetime
import pandas as pd
import random
import smtplib

my_email = "nmomce44@gmail.com"
my_password = "vntfgxmruewsfcqy"

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)
print(today_tuple)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {
    (data["month"], data["day"]): data_row for (index, data_row) in data.iterrows()
}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as files:
        contents = files.read()
        contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(smtp.gmail.com)
# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)




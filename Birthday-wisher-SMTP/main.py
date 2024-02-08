import smtplib

my_email = "nmomce44@gmail.com"
password = "vntfgxmruewsfcqy"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="tharry61@yahoo.com",
                        msg="subject: Hi Python study\n\n Whats new with python")

# go over to our gmail account and setup 2 factor authentication
# generate app password
# create a function to send email

from email.message import EmailMessage
from app2 import password
import ssl 
import smtplib



email_sender = '#####@gmail.com' # your email address
email_password = password # your email id password


email_receiver = '#######@gmail.com'

subject = "test email from python"

body = """this is a test email from python."""

#create instance for EmailMessage
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("email sent")




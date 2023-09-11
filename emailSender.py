# go over to our gmail account and setup 2 factor authentication
# generate app password
# create a function to send the email

from email.message import EmailMessage
from decouple import config
import ssl
import smtplib

email_sender = 'testdavjn@gmail.com'
email_password = config('password')

email_receiver = 'davidjrn63@gmail.com'

subject = "Don't forget to subscribe"
body = """ 
When you watch a video. bla bla
"""

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())



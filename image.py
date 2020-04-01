from smtplib import SMTP
import os
from email.message import EmailMessage
import imghdr

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'hello'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'pratimasingh160101@gmail.com'
msg.set_content('mail')
with open('Screenshot (66).png', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with SMTP('smtp.gmail.com', 587) as smtp:
#with SMTP('localhost', 1025) as smtp:

    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

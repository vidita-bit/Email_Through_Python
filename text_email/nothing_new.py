from smtplib import SMTP
import os
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'email seekh rhi hun'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'angelagarwal63@gmail.com'
msg.set_content('jldi seekh jaungi dont panic')

with SMTP('smtp.gmail.com', 587) as smtp:
#with SMTP('localhost', 1025) as smtp:

    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

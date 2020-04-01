from smtplib import SMTP
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
#with SMTP('smtp.gmail.com', 587) as smtp:
with SMTP('localhost', 1025) as smtp:

    #smtp.ehlo()
    #smtp.starttls()
    #smtp.ehlo()
    #smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'hi'
    body = 'done email with subject specified '

    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, 'angelagarwal63@gmail.com', msg)
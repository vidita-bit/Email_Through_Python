import ssl
from smtplib import SMTP_SSL
smtp_server = 'smtp.gmail.com'
port = 465
sender = 'viditaagrawal77@gmail.com'
password = input('enter ur password here:')
receiver = 'angelagarwal63@gmail.com'
message = """\
From: {}
To: {}
hello!
python here
""".format(sender, receiver)
context = ssl.create_default_context()
with SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)



#<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggDyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cv/iJTQUChcWr7x9Jv"
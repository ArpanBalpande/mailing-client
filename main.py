import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('<your-email>@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Arpan Balpande'
msg['To'] = 'testmails@spaml.de'
msg['Subject'] = "This is some test with Python"

with open('message.txt', 'r') as f:
    message = f.read()
msg.attach(MIMEText(message, 'plain'))

filename = 'Code.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('<your-email>@gmail.com', 'testmails@spaml.de', text)
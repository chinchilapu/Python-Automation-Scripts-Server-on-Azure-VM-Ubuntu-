import smtplib
import ssl
from email.message import EmailMessage
from datetime import datetime
fperson = "gmail" #The email to send from
password = "enter password"  
receiver = fperson #The email to send to, same as the sender in this instance
msg = EmailMessage()
msg[Sub] = "Daily Motivation" #Subject
msg[From] = fperson
msg[To] = receiver

msg.set_content(fNo pain, No gain\n\nSent on: {datetime.now()}) #Set Main contents of the email

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp.gmail.com, 465, context=context) as server: #gmail server
    server.login(fperson, password) #login
    server.send_message(msg) #Send the message

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import random

# Email details - replace with your info
sender_email = "your-email@gmail.com"
receiver_email = "your-email@gmail.com"
password = "your-app-password"  # Gmail app password (not your normal password)

# Create message
message = MIMEMultipart("alternative")
message["Subject"] = "Your Daily Motivational Quote"
message["From"] = sender_email
message["To"] = receiver_email

quotes = [
    "Failure is steeping stone to success.",
    "Success is not a destination, it's a journey.",
    "Nothing is impossible. The word itself says 'I'm possible!.",
    "The best time to start was yesterday. The next best is now."
]

quote = random.choice(quotes)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
text = f"Hi there!\n\nYour daily quote is:\n\n\"{quote}\"\n\nSent at {timestamp}"
message.attach(MIMEText(text, "plain"))

# Send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

# Log the quote sent
with open("/home/azureuser/quote_log.txt", "a") as f:
    f.write(f"[{timestamp}] {quote}\n")

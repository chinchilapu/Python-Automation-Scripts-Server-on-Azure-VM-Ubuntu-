#Install Azure CLI on Windows Go to windows powershell 
winget install --exact --id Microsoft.AzureCLI

#Run the azure cli
az login

#Create VM
az vm create --resource-group MyResourceGroup --name MyVM --image Ubuntu2204 --admin-username azureuser --generate-ssh-keys --size Standard_B1s

#a unquie ip will be generated add the ip address
ssh azureuser@<public-ip>

#Create a VM Environment
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y

#create your python automation script
mkdir -p ~/scripts
nano ~/scripts/daily_quote_email.py

#code
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import random

sender_email = "your-email@gmail.com"
receiver_email = "your-email@gmail.com"
password = "your-app-password"  

message = MIMEMultipart("alternative")
message["Subject"] = "Your Daily Motivational Quote"
message["From"] = sender_email
message["To"] = receiver_email

quotes = [

    "Failures are stepping stone to success.",
    "Success is not a destination, it's a journey.",
    "The best time to start was yesterday. The next best is now."
    
]

quote = random.choice(quotes)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
text = f"Hi there!\n\nYour daily quote is:\n\n\"{quote}\"\n\nSent at {timestamp}"
message.attach(MIMEText(text, "plain"))

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

with open("/home/azureuser/quote_log.txt", "a") as f:
    f.write(f"[{timestamp}] {quote}\n")





python3 ~/scripts/daily_quote_email.py
cat /home/azureuser/quote_log.txt

#schedule the script with cron
crontab -e

0 9 * * * /usr/bin/python3 /home/azureuser/scripts/daily_quote_email.py >> /home/azureuser/scripts/daily_quote_email.log 2>&1

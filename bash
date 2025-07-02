#create azure virtual machine
az vm create --resource-group MyResourceGroup --name MyVM --image Ubuntu2204 --admin-username azureuser --generate-ssh-keys --size Standard_B1s
ssh azureuser@<public-ip>
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
mkdir -p ~/scripts
nano ~/scripts/daily_quote_email.py
#test the script
python3 ~/scripts/daily_quote_email.py
cat /home/azureuser/quote_log.txt
crontab -e

# python3-Kite-Trade-Connect-login-Auto
python3 script for Kite Trade Connect login Auto which is required for everyday login before market start.

#I working with Linux Ubuntu 18.04 and here is installation step.

#Move to installation directory ( I am tried at /var/www/html/kite )

cd /var/www/html/kite

sudo apt install python3-pip

sudo pip3 install selenium

sudo pip3 install pyvirtualdisplay

wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz

tar -xvzf geckodriver*

chmod +x geckodriver

#set path for geckodriver
export PATH=$PATH:/var/www/html/kite/.

#install firefox.
sudo apt install firefox
firefox --version

#after that run script 
python3 kite.py

#you can see the capture of redirect page of kite trade. in capture.png
##############################
API_KEY = Which is provided by Kite.
USERiD = Which is provided by Kite.
PASSwORD = Which is set by account admin.
PiN = Which is set by account admin.

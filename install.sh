#!/bin/bash

sudo apt-get install pip
sudo pip install virtualenv virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv --no-site-packages gala2015
workon gala2015
pip install -r requirements.txt
add2virtualenv .
cp config.py{.example,}
echo "Edit your config.py file with the Google Spreadshet csv export url"

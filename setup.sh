#author: Hadaytullah Kundi
# Ubuntu 14.04, Trustysudo apt-get install mongodb-org mongodb-org-server

sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get
sudo apt-get install python3.6

# MongoDB

# clean any previous mongodb installation
sudo apt-get remove mongodb-org mongodb-org-server

sudo apt-get autoremove

sudo rm -rf /usr/bin/mongo*

# installation of mongodb begins
echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

sudo apt-get update

sudo apt-get install mongodb-org mongodb-org-server

sudo touch /etc/init.d/mongod

sudo apt-get install mongodb-org-server

#Flask setup
export FLASK_APP=app.py
export FLASK_ENV=development #change to production when in production

#To run the app
#flask run -p 8080 
#OR
#python3 app.py

#Development: on cloud 9 server just press run button

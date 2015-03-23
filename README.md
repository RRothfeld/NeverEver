# NeverEver web application
==============

Info
-------------

The NeverEver web application is a representation of the classic game "Never have I ever" providing easy access to the game via any web enabled device. 

Installation
--------------

The NeverEver web application is built using a range of technologies and requires the following pip set up:

	Django==1.7
	dnspython==1.12.0
	ecdsa==0.13
	Electrum==2.0.1
	pbkdf2==1.3
	pbr==0.10.7
	protobuf==3.0.0a1
	pyasn1==0.1.7
	pyasn1-modules==0.0.5
	qrcode==5.1
	requests==2.5.3
	six==1.9.0
	slowaes==0.1a1
	stevedore==1.2.0
	tlslite==0.4.8
	virtualenv==12.0.7
	virtualenv-clone==0.2.5
	virtualenvwrapper==4.3.2

To install the application you must first configure your virtualenv with the above set up. The following commands will allow you to import the above pip setup:
	
	pip install -r /path/to/requirements.txt

Once installed in your virtual environment, delete any existing migrations and issue the following commands

	python manage.py makemigrations neverever
	python manage.py migrate
	python populationScript.py
	python manage.py createsuperuser (make admin admin)
	python manage.py runserver

This will host the website on your localhost at the following address: 127.0.0.1:8000

Deployment
-------------

We have also included a number of production features to ensure successful deployment.

The deleteOldSessions.py file should be scheduled to run once per hour to delete idle sessions using the following command:

	python deleteOldSessions.py 

If you wish to reset the database issue the following:

	python emptyDBScript.py

never/**ever** Instructions
------------

From the homepage, a new game can be started by pressing the play button.

Once on the play screen, new users can be added by pressing the add player button and player names can be updated by entering them above each players response button. Use the submit button to navigate between questions once each player has responded. 

When you are finished your game, press the Your Stats button to be shown each of your responses. Here you will also be presented with an opportunity to fill in some more info on each of the players. 
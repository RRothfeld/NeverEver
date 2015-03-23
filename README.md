# NeverEver web application
--------------
never/ever is a web application which represents the classic drinking game "Never have I ever...". This web app is an 
assessed team project for the course Internet Technology (M) at the University of Glasgow.

We aimed at developing an app that facilitate social interaction in a fun, engaging, and interactive way; brings people
back together; and is intuitive in usage. You can play this game on any web enabled device!

So get together with some friends, grab a few drinks, and play some never/ever. You'll learn new things about your best
friends which you never actually wanted to know - but now you do! So, have fun and enjoy our game.

Installations
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

Once installed in your virtual environment, **delete any existing migrations** and issue the following commands

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

Testing
----------------

To test the application we have gone through a number of scenarios manually and tested the outcome to test whether it is as expected by using the Django admin page. 

From the homepage, clicking on the Play button starts a new session with a single player as expected. By clicking the add player button a new player is added in the models. When a game is finished, the Results model is updated with info on all the answers provided, including information about each of the players if this has been provided. Looking at the admin page at this point confirms that the session has been deleted (including the players) and the Results model is updated with info on the answers that have been provided. 

From the homepage when the Add statement button is clicked, users are able to add a statement which is then included in the statements model. If users miss any neccessary info, this is highlighted to them accordingly. 


# never/ever web application
never/ever is a web application which represents the classic drinking game "Never have I ever...". This web app is an 
assessed team project for the course **Internet Technology (M)** at the University of Glasgow.

We aimed at developing an app that facilitate social interaction in a fun, engaging, and interactive way; brings people
back together; and is intuitive in usage. You can play this game on any web enabled device!

So get together with some friends, grab a few drinks, and play some never/ever. You'll learn new things about your best
friends which you never actually wanted to know - but now you do! So, have fun and enjoy our game.

Installation
--------------
never/ever is built using a range of technologies (i.e. especially **Django**) and requires a specific **pip** setup. Install 
pip on your local computer. Once all pip and **Python 2.7.5** is installed, you are ready to activate our application. 
To do so, you must first configure your virtualenv with our pip requirements, which can be found as pip-requirements.txt 
in our repository. Download the web application and unzip the file in a local folder of your choosing. Afterwards, 
start a terminal and navigate to the used folder. Then, execute the following command within the downloaded 
folder as to allow you to import the pip setup and start the actual application:
	
	pip install -r pip-requirements.txt

Once pip is set up and Django working, issue the following commands:

	python manage.py makemigrations neverever
	python manage.py migrate
	python populationScript.py
	
Technically, the web application is now able to run locally. To be able to access the Django administration features 
however, you should create an admin account using the following command (you can use "admin" as name and password for local 
testing):
	
	python manage.py createsuperuser
	
Alright, your local web application is ready to be played. Simply start the application by issuing the following 
command:

	python manage.py runserver

This will host the app locally and can then be reached via: **http://127.0.0.1:8000/**

Maintaining Deployment
-------------
We have included additional production features to ensure successful, long-term deployment.

The deleteOldSessions.py file should be scheduled to run once per hour to delete idle sessions using the following command:

	python deleteOldSessions.py 

If you wish to reset the database issue the following:

	python emptyDBScript.py

Playing/Using Instructions
------------
From the homepage, a new game can be started by pressing the *PLAY* button.

Once on the play screen, new users can be added by pressing the *ADD PLAYER* button and player names can be updated by 
clicking above each players' response buttons. Use the *NEXT STATEMENT* button to continue to the next questions once 
each player has marked their answer to the given statement using the provided switches. 

When you are finished with your game, press the *YOUR STATS* button as to access a few statistics about your game. 
Here you will also be presented with an opportunity to fill in some more information on each of the players and, 
ultimately, are able to close the session of the game. Alternatively, you can just close any browser - after on hour
of inactivity, your session is automatically being closed for you.

If you wish to add a new statement to the game, simply press *NEW STATEMENT* and follow the on screen instructions.

Application Testing
----------------
To test the application we have gone through a number of scenarios manually and tested the outcome to test whether it 
is as expected by using the Django admin page. 

From the homepage, clicking on the Play button starts a new session with a single player as expected. By clicking the 
add player button a new player is added in the models. When a game is finished, the Results model is updated with info 
on all the answers provided, including information about each of the players if this has been provided. Looking at the 
admin page at this point confirms that the session has been deleted (including the players) and the Results model is 
updated with info on the answers that have been provided. 

From the homepage when the Add statement button is clicked, users are able to add a statement which is then included in 
the statements model. If users miss any necessary info, this is highlighted to them accordingly. 


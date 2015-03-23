# NeverEver web application
==============

Internet Technology Team Project

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


- python manage.py makemigrations neverever
- python manage.py migrate
- python populationScript.py
- python manage.py createsuperuser (make admin admin)
- python manage.py runserver

- run deleteOldSessions.py once every hour (to delete idle sessions)

- if you wish to reset the database, run emptyDBScript.py

- pip file can be found in folder

Testing
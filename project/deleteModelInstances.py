__author__ = 'Ram'

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()

from neverever.models import Category, Statement, Session, Player, Answer

# Delete Statements
print "Statements: {} instances were detected".format(Statement.objects.all().count())
Statement.objects.all().delete()
print "Statements: {} instances remain".format(Statement.objects.all().count())

# Delete Categories
print "Categories: {} instances were detected".format(Category.objects.all().count())
Category.objects.all().delete()
print "Categories: {} instances remain".format(Category.objects.all().count())

# Delete Sessions
print "Sessions: {} instances were detected".format(Session.objects.all().count())
Session.objects.all().delete()
print "Sessions: {} instances remain".format(Session.objects.all().count())

# Delete Players
print "Players: {} instances were detected".format(Player.objects.all().count())
Player.objects.all().delete()
print "Players: {} instances remain".format(Player.objects.all().count())

# Delete Answers
print "Answers: {} instances were detected".format(Answer.objects.all().count())
Answer.objects.all().delete()
print "Answers: {} instances remain".format(Answer.objects.all().count())
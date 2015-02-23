__author__ = 'Ram'

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()

from neverever.models import Category, Statement, Session, Player, Anwser

# Delete Statements
print "Statements: {} instances were detected".format(Statement.objects.all().count())
Statement.objects.all().delete()
print "Statements: {} instances remain".format(Statement.objects.all().count())

# Delete Categories
print "Categories: {} instances were detected".format(Category.objects.all().count())
Category.objects.all().delete()
print "Categories: {} instances remain".format(Category.objects.all().count())
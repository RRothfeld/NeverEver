import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()

from neverever.models import Category, Statement, Session, Player, Answer, GlobalCounter, Result

nstatements = Statement.objects.all().count()
ncategories = Category.objects.all().count()
nsessions = Session.objects.all().count()
nplayers = Player.objects.all().count()
nanswers = Answer.objects.all().count()
nresults = Result.objects.all().count()
nglobalcounter = GlobalCounter.objects.all().count()

# Delete Statements
print "Statements: {} instances were detected".format(nstatements)
Statement.objects.all().delete()
print "Statements: {} instances remain".format(Statement.objects.all().count())

# Delete Categories
print "Categories: {} instances were detected".format(ncategories)
Category.objects.all().delete()
print "Categories: {} instances remain".format(Category.objects.all().count())

# Delete Sessions
print "Sessions: {} instances were detected".format(nsessions)
Session.objects.all().delete()
print "Sessions: {} instances remain".format(Session.objects.all().count())

# Delete Players
print "Players: {} instances were detected".format(nplayers)
Player.objects.all().delete()
print "Players: {} instances remain".format(Player.objects.all().count())

# Delete Answers
print "Answers: {} instances were detected".format(nanswers)
Answer.objects.all().delete()
print "Answers: {} instances remain".format(Answer.objects.all().count())

# Delete Results
print "Results: {} instances were detected".format(nresults)
Result.objects.all().delete()
print "Results: {} instances remain".format(Result.objects.all().count())

# Delete GlobalCounter
print "GlobalCounter: {} instances were detected".format(nglobalcounter)
GlobalCounter.objects.all().delete()
print "GlobalCounter: {} instances remain".format(GlobalCounter.objects.all().count())
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()

from neverever.models import Session, Result, Answer

from datetime import datetime, timedelta

num_hours = 1

sessions = Session.objects.filter(last_modified__lte=datetime.now()-timedelta(hours=num_hours))

# # debug line below to just bring in all sessions
# sessions = Session.objects.all()
# print sessions

allAnswers = Answer.objects.all()

for answer in allAnswers:
    if answer.session in sessions:
        statement = answer.statement
        result = answer.answer
        result = Result.objects.create(statement=statement, answer=result)


# print len(sessions), " old sessions were detected"

sessions.delete()

# print len(sessions), " old sessions remain"
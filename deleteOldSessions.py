import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()

from neverever.models import Session, Result

from datetime import datetime, timedelta

num_hours = 1

# sessions = Session.objects.filter(last_modified__lte=datetime.now()-timedelta(hours=num_hours))

# debug line below to just bring in all sessions
sessions = Session.objects.all()
print sessions

for session in sessions:
    questions = session.used_statements.all()
    for question in questions:
        statement = question
        result = Result.objects.create(statement=statement)

# print len(sessions), " old sessions were detected"

sessions.delete()

# print len(sessions), " old sessions remain"
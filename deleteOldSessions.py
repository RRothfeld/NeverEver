import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()

from neverever.models import Session, Result, Answer

from datetime import datetime, timedelta

num_hours = 1


sessions = Session.objects.filter(last_modified__lte=datetime.now()-timedelta(hours=num_hours))
for session in sessions:
    answers = Answer.objects.filter(player__session=session)
    for answer in answers:
        Result.objects.create(statement=answer.statement, answer=answer.answer, gender=answer.player.gender,
                              nationality=answer.player.nationality, age=answer.player.age)

sessions.delete()
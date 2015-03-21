import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()

from neverever.models import Session

from datetime import datetime, timedelta

num_hours = 1

sessions = Session.objects.filter(last_modified__lte=datetime.now()-timedelta(hours=num_hours))

# print len(sessions), " old sessions were detected"

sessions.delete()

# print len(sessions), " old sessions remain"
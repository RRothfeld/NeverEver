# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neverhaveiever', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
        migrations.AddField(
            model_name='category',
            name='adult_themed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='statement',
            name='yes_answers',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

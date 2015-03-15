# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neverever', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='num_players',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neverever', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statement',
            name='category',
        ),
        migrations.AddField(
            model_name='statement',
            name='categories',
            field=models.ManyToManyField(to='neverever.Category'),
            preserve_default=True,
        ),
    ]

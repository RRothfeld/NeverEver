# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neverever', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='player',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='session',
            name='slug',
        ),
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
    ]

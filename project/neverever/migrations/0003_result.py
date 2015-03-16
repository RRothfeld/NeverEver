# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neverever', '0002_session_num_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=128, null=True)),
                ('age', models.IntegerField(null=True)),
                ('nationality', models.CharField(max_length=128, null=True)),
                ('answer', models.BooleanField(default=False)),
                ('statement', models.ForeignKey(to='neverever.Statement')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

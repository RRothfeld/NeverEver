# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('adult_themed', models.BooleanField(default=False)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('no_answers', models.IntegerField(default=0)),
                ('yes_answers', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(to='neverhaveiever.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

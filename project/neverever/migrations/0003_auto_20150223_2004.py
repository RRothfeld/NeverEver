# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neverever', '0002_auto_20150215_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('answer', models.BooleanField(default=False)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('gender', models.CharField(max_length=1)),
                ('age', models.IntegerField()),
                ('nationality', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('statements', models.ManyToManyField(to='neverever.Statement')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='session',
            field=models.ManyToManyField(to='neverever.Session'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='player',
            field=models.ManyToManyField(to='neverever.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='session',
            field=models.ManyToManyField(to='neverever.Session'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='statement',
            field=models.ManyToManyField(to='neverever.Statement'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='category',
            name='adult_themed',
        ),
        migrations.RemoveField(
            model_name='statement',
            name='no_answers',
        ),
        migrations.RemoveField(
            model_name='statement',
            name='yes_answers',
        ),
        migrations.AlterField(
            model_name='statement',
            name='title',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]

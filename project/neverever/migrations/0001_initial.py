# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=1, null=True)),
                ('age', models.IntegerField(null=True)),
                ('nationality', models.CharField(max_length=128, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('categories', models.ManyToManyField(to='neverever.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='session',
            name='statements',
            field=models.ManyToManyField(to='neverever.Statement'),
            preserve_default=True,
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
    ]

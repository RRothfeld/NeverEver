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
                ('stamp', models.IntegerField(serialize=False, primary_key=True)),
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
            name='GlobalCounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_sessions', models.IntegerField()),
                ('total_players', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stamp', models.IntegerField()),
                ('gender', models.CharField(max_length=1, null=True)),
                ('age', models.IntegerField(null=True)),
                ('nationality', models.CharField(max_length=128, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=128, null=True)),
                ('age', models.IntegerField(null=True)),
                ('nationality', models.CharField(max_length=128, null=True)),
                ('answer', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sid', models.CharField(max_length=128, null=True)),
                ('nsfw', models.BooleanField(default=False)),
                ('num_players', models.IntegerField(default=1)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='neverever.Category')),
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
                ('likes', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('nsfw', models.BooleanField(default=True)),
                ('categories', models.ManyToManyField(to='neverever.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='session',
            name='last_statement',
            field=models.ForeignKey(related_name=b'last_statement', to='neverever.Statement', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='session',
            name='used_statements',
            field=models.ManyToManyField(related_name=b'used_statements', null=True, to='neverever.Statement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='result',
            name='statement',
            field=models.ForeignKey(to='neverever.Statement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='session',
            field=models.ForeignKey(to='neverever.Session'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='player',
            field=models.ForeignKey(to='neverever.Player', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='session',
            field=models.ForeignKey(to='neverever.Session', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='statement',
            field=models.ForeignKey(to='neverever.Statement', null=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neverever', '0003_result'),
    ]

    operations = [
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
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neverhaveiever', '0002_category_adult_themed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
    ]

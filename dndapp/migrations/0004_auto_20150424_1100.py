# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dndapp', '0003_auto_20150424_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterclass',
            name='class_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='race',
            name='race_name',
            field=models.CharField(max_length=20),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('dndapp', '0005_auto_20150428_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(unique=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='race',
            name='charisma',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)], default=0),
        ),
        migrations.AlterField(
            model_name='race',
            name='constitution',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)], default=0),
        ),
        migrations.AlterField(
            model_name='race',
            name='dexterity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)], default=0),
        ),
        migrations.AlterField(
            model_name='race',
            name='intelligence',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)], default=0),
        ),
        migrations.AlterField(
            model_name='race',
            name='strength',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)], default=0),
        ),
        migrations.AlterField(
            model_name='race',
            name='wisdom',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)], default=0),
        ),
    ]

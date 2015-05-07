# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('strength', models.IntegerField(validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(18)])),
                ('dexterity', models.IntegerField(validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(18)])),
                ('constitution', models.IntegerField(validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(18)])),
                ('wisdom', models.IntegerField(validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(18)])),
                ('intelligence', models.IntegerField(validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(18)])),
                ('charisma', models.IntegerField(validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(18)])),
            ],
        ),
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('playername', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='character_class',
            field=models.ForeignKey(to='dndapp.CharacterClass'),
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.ForeignKey(to='dndapp.Race'),
        ),
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.ForeignKey(to='dndapp.User'),
        ),
    ]

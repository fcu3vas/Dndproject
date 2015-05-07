# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dndapp', '0002_auto_20150423_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterclass',
            name='class_name',
            field=models.CharField(max_length=3, choices=[('BBN', 'Barbarian'), ('BRD', 'Bard'), ('CLR', 'Cleric'), ('DRD', 'Druid'), ('FTR', 'Fighter'), ('MNK', 'Monk'), ('PAL', 'Paladin'), ('RGR', 'Ranger'), ('ROG', 'Rogue'), ('SOR', 'Sorcerer'), ('WIZ', 'Wizard'), ('WCK', 'Warlock')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='race_name',
            field=models.CharField(max_length=4, choices=[('DRG', 'Dragonborn'), ('DWF', 'Dwarf'), ('ELF', 'Elf'), ('GNM', 'Gnome'), ('HE', 'Half-elf'), ('HO', 'Half-orc'), ('HALF', 'Halfling'), ('HUM', 'Human'), ('TFL', 'Tiefling')]),
        ),
    ]

from collections import OrderedDict
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

attribute_fields = ['strength', 'dexterity', 'constitution', 'wisdom', 'intelligence', 'charisma']


class Gender(object):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


class User(models.Model):
    playername = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.playername


class Race(models.Model):
    race_name = models.CharField(max_length=20)
    strength = models.IntegerField(default=0, null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(2)])
    dexterity = models.IntegerField(default=0, null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(2)])
    constitution = models.IntegerField(default=0, null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(2)])
    wisdom = models.IntegerField(default=0, null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(2)])
    intelligence = models.IntegerField(default=0, null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(2)])
    charisma = models.IntegerField(default=0, null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(2)])

    def __str__(self):
        return self.race_name


class CharacterClass(models.Model):
    class_name = models.CharField(max_length=20)

    def __str__(self):
        return self.class_name


class Character(models.Model):

    character_info_order = OrderedDict([('user', 'User'), ('name', 'Name'), ('gender', 'Gender'), ('race', 'Race'),
                                        ('character_class', 'Class'), ('strength', 'Str'), ('dexterity', 'Dex'),
                                        ('constitution', 'Con'), ('wisdom', 'Wis'), ('intelligence', 'Int'),
                                        ('charisma', 'Cha')])

    user = models.ForeignKey(User)
    name = models.CharField(max_length=30, null=False, blank=False, unique=True)
    gender = models.CharField(max_length=1, choices=Gender.GENDER_CHOICES)
    character_class = models.ForeignKey(CharacterClass)
    race = models.ForeignKey(Race)
    strength = models.IntegerField(validators=[MinValueValidator(6), MaxValueValidator(18)])
    dexterity = models.IntegerField(validators=[MinValueValidator(6), MaxValueValidator(18)])
    constitution = models.IntegerField(validators=[MinValueValidator(6), MaxValueValidator(18)])
    wisdom = models.IntegerField(validators=[MinValueValidator(6), MaxValueValidator(18)])
    intelligence = models.IntegerField(validators=[MinValueValidator(6), MaxValueValidator(18)])
    charisma = models.IntegerField(validators=[MinValueValidator(6), MaxValueValidator(18)])

    def __str__(self):
        return self.name

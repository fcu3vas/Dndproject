from dndapp.models import attribute_fields
import random


def modify_attributes(character):
    for attribute in attribute_fields:
        setattr(character, attribute, getattr(character, attribute) + getattr(character.race, attribute))
    return character


def initial_attribute():
    return {field: dice_rolling() for field in attribute_fields}

def dice_rolling():
    dicerolls = [random.randint(2, 6) for roll in range(4)]
    dicerolls.sort()
    dicerolls = dicerolls[1:]
    return sum(dicerolls)


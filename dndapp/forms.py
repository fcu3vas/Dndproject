from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ('user', 'name', 'gender', 'character_class', 'race', 'strength', 'dexterity',
                  'constitution', 'wisdom', 'intelligence', 'charisma',)

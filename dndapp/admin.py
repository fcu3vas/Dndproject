from django.contrib import admin
from .models import User, Race, CharacterClass, Character

admin.site.register(User)
admin.site.register(Race)
admin.site.register(CharacterClass)
admin.site.register(Character)

from django.shortcuts import render, redirect
from dndapp.models import Character
from dndapp.utils import modify_attributes, initial_attribute
from .forms import CharacterForm



def char_list(request):
    character_table = []
    characters = Character.objects.all()
    for character in characters:
        character_table.append(tuple(getattr(character, field) for field in Character.character_info_order))
    return render(request, 'dndapp/char_list.html', {'field_order': Character.character_info_order.values(),
                                                     'character_table': character_table})


def new_char(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            modify_attributes(character)
            character.save()
            return redirect('/')
    else:
        form = CharacterForm(initial=initial_attribute())
    return render(request, 'dndapp/new_char.html', {'form': form})






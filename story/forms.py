# In your forms.py file

from django import forms
from .models import Genre, Story

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['title', 'slug', 'description']

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'genre', 'story', 'photo']

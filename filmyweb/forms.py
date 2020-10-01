from django.forms import ModelForm
from django import forms
from .models import Film, Comments

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['tytul', 'opis', 'premiera', 'rok', 'imbd_rating', 'plakat']

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['komentarz']


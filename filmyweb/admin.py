from django.contrib import admin
from .models import Film, Comments


# Register your models here.

@admin.register(Film)

class FilmAdmin(admin.ModelAdmin):
    #fields = ["tytul", "opis", "rok"]
    #exclude = ["opis"]
    list_display = ["tytul", "imbd_rating", "rok"]
    list_filter = ("rok", "imbd_rating")
    search_fields = ("tytul", "opis")

admin.site.register(Comments)
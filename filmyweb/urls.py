from django.urls import path
from filmyweb.views import wszystkie_filmy, nowy_film, usun_film, edytuj_film, pojedynczy, comment_remove


urlpatterns = [
    path('wszystkie/', wszystkie_filmy, name="wszystkie"),
    path('nowy/', nowy_film, name="nowy_film"),
    path('usun/<int:id>/', usun_film, name="usun_film"),
    path('edytuj/<int:id>/', edytuj_film, name="edytuj_film"),
    path('pojedynczy/<int:id>/', pojedynczy, name="pojedynczy"),
    path('pojedynczy/<int:pk>/remove/', comment_remove, name='comment_remove'),

]
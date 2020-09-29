from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Film, Comments
import random
from django.db.models import Q
from .forms import FilmForm, CommentForm
from django.contrib.auth.decorators import login_required

def wszystkie_filmy(request):
    wszystkie = Film.objects.all()
    ilosc = len(Film.objects.all())
    tab = []
    for e in Film.objects.all():
        tab.append(e.id)

    losowy = Film.objects.get(id=(random.choice(tab)))

    return render(request, 'filmy.html', {'filmy': wszystkie, 'losowy': losowy, 'ilosc': ilosc})

def likeviews(request, id):
    film = get_object_or_404(Film, id=request.POST.get('post_id'))
    film.likes.add(request.user.id)
    return redirect(pojedynczy, id=film.pk)

def pojedynczy(request, id):
    film = get_object_or_404(Film, pk=id)
    ilosc = len(Film.objects.all())
    total_likes = film.total_likes()
    tab = []
    for e in Film.objects.all():
        tab.append(e.id)
    losowy = get_object_or_404(Film, id=(random.choice(tab)))
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = film
            comment.aut = request.user
            comment.save()
            
        else:
            form = CommentForm()


    return render(request, 'pojedynczy.html', {'total_likes': total_likes, 'film': film, 'losowy': losowy,'ilosc': ilosc,'form': form  })

@login_required()
def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'nowy.html', {'form' : form, 'nowy': True})

@login_required()
def edytuj_film(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)
    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)
    return render(request, 'edytuj.html', {'form': form, 'film': film, 'nowy': False})

@login_required()
def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)
    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)
    return render(request, 'potwierdz.html', {'film': film})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comments, pk=pk)
    comment.delete()
    return redirect(pojedynczy, id=comment.post.pk)

class SearchResultsView(ListView):
    model = Film
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Film.objects.filter(Q(tytul__icontains=query))
        return object_list
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Movie
import random

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context={
        "movies":movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie=get_object_or_404(Movie, pk=movie_pk)
    context={
        "movie": movie,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    if request.user.is_authenticated:
        movies = list(Movie.objects.all())
        movies= random.sample(movies, 10)
        context={
            "movies":movies,
        }
        return render(request, 'movies/recommended.html', context)
    return redirect('accounts:login')
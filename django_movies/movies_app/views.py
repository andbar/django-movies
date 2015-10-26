from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import ListView, DetailView
from movies_app.models import Movie, Rater, Rating
from django.db.models import Avg


def index_view(request):
    movies = sorted(Movie.objects.all(), key=lambda x: x.avg_rating, reverse=True)
    context = {'movies': movies[0:20]}
    return render_to_response(template_name="index.html", context=context)

class MovieList(ListView):
    model = Movie

class MovieDetails(DetailView):
    model = Movie

class RaterList(ListView):
    model = Rater

class RaterDetails(DetailView):
    model = Rater


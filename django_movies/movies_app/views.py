from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import ListView, DetailView
from movies_app.models import Movie, Rater, Rating


def index_view(request):
    return render_to_response(template_name="base.html", context={})

class MovieList(ListView):
    model = Movie

class MovieDetails(DetailView):
    model = Movie

class RaterList(ListView):
    model = Rater

class RaterDetails(DetailView):
    model = Rater

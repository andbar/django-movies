from django.db import models

# Create your models here.
from django.db.models import Avg


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return str(self.age) + self.gender + self.zip_code + self.occupation

    def _get_avg_rating(self):
        avg_rating = self.rating_set.aggregate(Avg('rating_num'))
        return avg_rating["rating_num__avg"]

    avg_rating = property(_get_avg_rating)

    def _get_movies(self):
        movies = []
        for rating in self.rating_set.all():
            movies.append({"movie_id": rating.movie.id, "title": rating.movie.title, "rating_num": rating.rating_num})
        return movies

    movies = property(_get_movies)


class MovieManager(models.Manager):

    def top_twenty(self):
        top_movies = []
        for movie in Movie.objects.all():
            if movie.count_rating >= 25:
                top_movies.append(movie)
        return sorted(top_movies, key=lambda x: x.avg_rating, reverse=True)[:20]


class Movie(models.Model):
    title = models.CharField(max_length=100)

    objects = MovieManager()

    class Meta:
        ordering = ["title"]

    def _get_rating_count(self):
        return self.rating_set.count()

    count_rating = property(_get_rating_count)

    def _get_avg_rating(self):
        avg_rating = self.rating_set.aggregate(Avg('rating_num'))
        return avg_rating["rating_num__avg"]

    avg_rating = property(_get_avg_rating)

    def _get_raters(self):
        raters = []
        for rating in self.rating_set.all():
            raters.append({"rater_id": rating.rater.id, "rating_num": rating.rating_num})
        return raters

    raters = property(_get_raters)

    def __str__(self):
        return self.title


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating_num = models.IntegerField(choices=[(1, "Terrible"), (2, "Okay"), (3, "Good"), (4, "Great"), (5, "Awesome")])

    def __str__(self):
        return self.movie.title + ": " + str(self.rating_num)

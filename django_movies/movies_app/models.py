from django.db import models

# Create your models here.


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return str(self.age) + self.gender + self.zip_code + self.occupation


class Movie(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating_num = models.IntegerField()

    def __str__(self):
        return self.movie.title + " " + str(self.rating_num)

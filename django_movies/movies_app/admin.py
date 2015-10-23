from django.contrib import admin

# Register your models here.
from movies_app.models import Rater, Movie, Rating

admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Rating)

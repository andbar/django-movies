"""django_movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from movies_app.views import MovieList, MovieDetails, index_view, RaterList, RaterDetails

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index_view, name="index"),
    url(r'^movies/$', MovieList.as_view(), name="movies_list"),
    url(r'^movies/(?P<pk>\d+)/$', MovieDetails.as_view(), name="movie_details"),
    url(r'^raters/$', RaterList.as_view(), name="raters_list"),
    url(r'^raters/(?P<pk>\d+)/$', RaterDetails.as_view(), name="rater_details")
]

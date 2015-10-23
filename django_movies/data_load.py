import pandas as pd


def load_raters(apps, schema_editor):
    raters = pd.read_csv("u.user", sep="|", header=None, names=["rater_id", "age", "gender", "occupation", "zip_code"])
    Rater = apps.get_model("movies_app", "Rater")
    for index, row in raters.iterrows():
        rater_id = row.rater_id
        age = row.age
        gender = row.gender
        occupation = row.occupation
        zip_code = row.zip_code
        Rater.objects.create(id=rater_id, age=age, gender=gender, occupation=occupation, zip_code=zip_code)


def load_movies(apps, schema_editor)   :
    movies = pd.read_csv("u.item", sep="|", header=None, encoding="windows-1252")
    movies.rename(columns={0: "movie_id", 1: "title"}, inplace=True)
    Movie = apps.get_model("movies_app", "Movie")
    for index, row in movies.iterrows():
        movie_id = row.movie_id
        title = row.title
        Movie.objects.create(id=movie_id, title=title)


def load_ratings(apps, schema_editor):
    ratings = pd.read_csv("u.data", sep="\t", header=None, names=["rater", "movie", "rating", "timestamp"])
    Rating = apps.get_model("movies_app", "Rating")
    Rater = apps.get_model("movies_app", "Rater")
    Movie = apps.get_model("movies_app", "Movie")
    for index, row in ratings.iterrows():
        rater = row.rater
        movie = row.movie
        rating_num = row.rating
        Rating.objects.create(rater=Rater.objects.get(id=rater), movie=Movie.objects.get(id=movie), rating_num=rating_num)

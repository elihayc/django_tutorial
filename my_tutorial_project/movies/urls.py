from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('movie_rating', views.movieRating, name='movie_rating'),
    path('common_movies', views.commonMovies, name='common_movies'),
]

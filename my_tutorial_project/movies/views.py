import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .managers.MovieManager import MovieManager


@require_http_methods(["GET"])
def index(request):
    return render(request, 'movies/index.html')


@require_http_methods(["GET"])
def movieRating(request):
    movie_name = request.GET.get("movie_name", None)
    movie = MovieManager().get_movie_rating(movie_name)

    if movie is not None:
        return JsonResponse(movie.asDict(), status=200)
    else:
        return HttpResponse('', status=200)


@require_http_methods(["GET"])
def commonMovies(request):
    actor1_name = request.GET.get("actor1", None)
    actor2_name = request.GET.get("actor2", None)

    common_movies = MovieManager().get_common_movies([actor1_name, actor2_name])

    json_list = []
    for movie in common_movies:
        json_list.append(movie)

    return JsonResponse(json_list, safe=False)

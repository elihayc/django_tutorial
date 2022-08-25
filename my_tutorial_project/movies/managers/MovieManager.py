from .IMDBClient import IMDBClient
from ..Helpers.Consts import MAX_MOVIE_NAME_LENGTH, ROLE_ACTOR, ROLE_ACTRESS
from ..models import Movie


class MovieManager:
    imdb_client = IMDBClient()

    def get_movie_rating(self, movie_name: str) -> Movie:
        if not self.__is_valid_movie_name(movie_name):
            raise Exception(f"Invalid movie name {movie_name}")

        movie: Movie = None
        movie_dict = self.imdb_client.search_movie(movie_name)

        if movie_dict is not None:
            movie = Movie(movie_id=movie_dict['id'],
                          title=movie_dict['title'],
                          image_url=movie_dict['image'],
                          description=movie_dict['description'],
                          rating=None)
            movie.rating = self.imdb_client.rating(movie.movie_id)

        return movie

    def get_common_movies(self, actors_names: [str]) -> [Movie]:
        titles = []
        for actor_name in actors_names:
            if not self.__is_valid_actor_name(actor_name):
                raise Exception(f"Invalid actor name {actor_name}")

        actors = self.imdb_client.search_names(actors_names)

        if len(actors) == len(actors_names):
            actors_ids = [actor['id'] for actor in actors]
            actor_details = self.imdb_client.name_details(actors_ids)

            if actor_details is not None and len(actor_details) == len(actors_names):
                casts_movies = [details['castMovies'] for details in actor_details]

                movies_ids_sets = []
                for cast_movie in casts_movies:
                    movie_ids_set = set(x['id'] for x in cast_movie if x['role'] == ROLE_ACTOR or x['role'] == ROLE_ACTRESS)
                    movies_ids_sets.append(movie_ids_set)

                intersection_ids = set.intersection(*movies_ids_sets)

                if len(intersection_ids) > 0:
                    titles = [value['title'] for value in casts_movies[0] if value['id'] in intersection_ids]
            else:
                raise Exception("failed on getting actor details for all actors")
        else:
            raise Exception("not all the actors were found")

        return titles

    def __is_valid_movie_name(self, movie_name) -> bool:
        return movie_name is not None and 0 < len(movie_name) <= MAX_MOVIE_NAME_LENGTH

    def __is_valid_actor_name(self, actor_name) -> bool:
        return actor_name is not None and 0 < len(actor_name) <= MAX_MOVIE_NAME_LENGTH

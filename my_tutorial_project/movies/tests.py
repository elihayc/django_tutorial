from unittest import TestCase

from django.urls import reverse

from my_tutorial_project.movies.managers.MovieManager import MovieManager


class MovieManagerTests(TestCase):

    def test_get_movie_rating_success(self):
        # Arrange
        movieManager = MovieManager()

        # Act
        movie = movieManager.get_movie_rating("Momento")

        # Assert
        self.assertEqual(movie.movie_id, 'tt3517344')
        self.assertEqual(movie.title, "Momento")
        self.assertEqual(movie.image_url,
                         'https://m.media-amazon.com/images/M/MV5BMzhmYzkwMDQtNzAyYi00YzRiLTg1NWEtMzI5MmIyYTcxY2QyXkEyXkFqcGdeQXVyNzQ5MzY0NjM@._V1_Ratio0.7273_AL_.jpg')
        self.assertEqual(movie.description, '(2013)')
        self.assertEqual(movie.rating, '7.6')

    def test_get_movie_rating_empty_name(self):
        # Arrange
        movieManager = MovieManager()

        # Act and Assert
        self.assertRaises(Exception, lambda: movieManager.get_movie_rating(""))

    def test_get_common_movies_1_movie(self):
        # Arrange
        movieManager = MovieManager()

        # Act
        movies = movieManager.get_common_movies(["mel gibson", "Natalie Portman"])

        # Assert
        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0], 'The Simpsons')

    def test_get_common_movies_8_movies(self):
            # Arrange
            movieManager = MovieManager()

            # Act
            movies = movieManager.get_common_movies(["Keanu Reeves", "Carrie-Anne Moss"])

            # Assert
            self.assertGreaterEqual(len(movies), 8)

    def test_get_common_movies_no_movies(self):
        # Arrange
        movieManager = MovieManager()

        # Act
        movies = movieManager.get_common_movies(["mel gibson", "Robert De Niro"])

        # Assert
        self.assertEqual(len(movies), 0)

    def test_get_common_movies_empty_actor_name(self):
        # Arrange
        movieManager = MovieManager()

        # Assert and Act
        self.assertRaises(Exception, lambda: movieManager.get_common_movies(["mel gibson", ""]))

    def test_get_common_movies_None_actor_name(self):
        # Arrange
        movieManager = MovieManager()

        # Assert and Act
        self.assertRaises(Exception, lambda: movieManager.get_common_movies(["mel gibson", None]))

    def test_get_common_movies_not_exist_actor_name(self):
        # Arrange
        movieManager = MovieManager()

        # Assert and Act
        self.assertRaises(Exception, lambda: movieManager.get_common_movies(["mel gibson", "zqzqzqzqzqzqzqzq"]))

    def test_get_common_movies_series(self):
        # Arrange
        movieManager = MovieManager()

        # Act
        movies = movieManager.get_common_movies(["leonardo dicaprio", "brad pitt"])

        # Assert
        self.assertEqual(len(movies), 3)


class Movie:
    movie_id: str
    title: str
    image_url: str
    description: str
    rating: str

    def __init__(self, movie_id: str, title: str, image_url: str, description: str, rating: str):
        self.movie_id = movie_id
        self.title = title
        self.image_url = image_url
        self.description = description
        self.rating = rating

    def asDict(self):
        return self.__dict__

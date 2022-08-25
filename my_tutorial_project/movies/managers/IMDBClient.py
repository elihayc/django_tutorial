from ..Helpers.RestClient import RestClient

imdb_token = "k_jqqasfh9"
# imdb_token = "k_v6g5qyxm"

imdb_API_prefix = "https://imdb-api.com/en/API/"


class IMDBClient:
    rest_client = RestClient()

    def search_movie(self, movie_name) -> dict:
        url = f"{imdb_API_prefix}SearchMovie/{imdb_token}/{movie_name}"

        result_json = self.rest_client.get_json_response(url)
        movie_dict = self.__get_results(result_json)

        return movie_dict

    def rating(self, movie_id) -> str:
        url = f"{imdb_API_prefix}Ratings/{imdb_token}/{movie_id}"
        result_json = self.rest_client.get_json_response(url)

        rating = result_json['imDb']

        return rating

    def search_names(self, actors_names: [str]) -> [dict]:
        urls = []
        for actor_name in actors_names:
            urls.append(f"{imdb_API_prefix}SearchName/{imdb_token}/{actor_name}")

        responses_json = self.rest_client.get_json_wait_all_urls(urls)

        actors = []
        for response_json in responses_json:
            actor = self.__get_results(response_json)
            if actor is not None:
                actors.append(actor)

        return actors

    def name_details(self, persons_ids: [str]) -> [dict]:
        urls = []
        for person_id in persons_ids:
            urls.append(f"{imdb_API_prefix}Name/{imdb_token}/{person_id}")

        responses_json = self.rest_client.get_json_wait_all_urls(urls)

        return responses_json

    def __get_results(self, response_json: str) -> str:
        if response_json is not None and "results" in response_json:
            results = response_json['results']
            if results is not None:
                if len(results) > 0:
                    item = response_json['results'][0]
                else:
                    item = None
                return item
            else:
                raise Exception(f"No items in the result {response_json}")
        else:
            raise Exception(f"Unexpected response {response_json}")

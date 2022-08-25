import asyncio
import aiohttp
import requests
from aiohttp import ClientResponse

from .Consts import HTTP_200_OK


class RestClient:

    def get_json_response(self, url):
        response = requests.get(url)

        if response.status_code == HTTP_200_OK:
            result_json = response.json()
        else:
            raise Exception(f"expected 200, but the status code: {response.status_code} for url: {url}")

        return result_json

    def get_json_wait_all_urls(self, urls: [str]) -> [object]:
        event_loop = asyncio.new_event_loop()
        responses_data = event_loop.run_until_complete(self.__get_all_responses(urls))

        return responses_data

    async def __get_all_responses(self, url_calls) -> [dict]:
        async with aiohttp.ClientSession() as session:
            tasks = self.__get_tasks_by_url_calls(session, url_calls)
            responses = await asyncio.gather(*tasks)

            results = []
            response: ClientResponse
            for response in responses:
                if response.status == HTTP_200_OK:
                    results.append(await response.json())
                else:
                    raise Exception(f"IMDB status code: {response.status} for url: {response.real_url}")

            return results

    def __get_tasks_by_url_calls(self, session, url_calls):
        tasks = []
        for url_call in url_calls:
            tasks.append(asyncio.create_task(session.get(url_call, ssl=False)))
        return tasks

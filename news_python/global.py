import requests
import json
from .news_api import News
import random


class Global:
    def __init__(self, key):
        self.key = key

    def get_news(self, query, source=None):
        """
        :param source:
        :param query:
        :return: Get a random news article worldwide
        """

        if not source:
            response = requests.get(url=f"http://newsapi.org/v2/top-headlines?"
                                        f"query={query.replace(' ', '%20')}&apiKey={self.key}")

        else:
            response = requests.get(url=f"http://newsapi.org/v2/top-headlines?"
                                        f"query={query.replace(' ', '%20')}&source=technology&apiKey={self.key}")

        news = json.loads(response.content)
        random_news = random.randint(0, len(news["articles"]) - 1)

        return News(
            status=news["status"],
            total_results=len(news["articles"]),
            publisher_name=news["articles"][random_news]["source"]["name"],
            published_at=news["articles"][random_news]["publishedAt"],
            author=news["articles"][random_news]["author"],
            title=news["articles"][random_news]["title"],
            description=news["articles"][random_news]["description"],
            content=news["articles"][random_news]["content"],
            url=news["articles"][random_news]["url"],
            url_to_image=news["articles"][random_news]["urlToImage"]
        )

import requests
import json
from .news_api import News
import random


class Country:
    def __init__(self, key):
        self.key = key

    def get_news(self, country, category=None):
        """
        :param category:
        :param country:
        :return: A random news from the selected country
        """

        if not category:
            response = requests.get(url=f"http://newsapi.org/v2/top-headlines?country={country}&apiKey={self.key}")

        else:
            response = requests.get(url=f"http://newsapi.org/v2/top-headlines?country={country}"
                                        f"&category={category.replace(' ', '%20')}&apiKey={self.key}")

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

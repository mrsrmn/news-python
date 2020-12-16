import requests
import json


class Country:
    def __init__(self, key):
        self.key = key

    def get_news(self, country):
        response = requests.get(url=f"http://newsapi.org/v2/top-headlines?country={country}&apiKey={self.key}")
        news = json.loads(response.content)
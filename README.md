# news-python

A Python API Wrapper for the https://newsapi.org/ JSON API

## Installation

To install news-python, simply use:

`pip install news-python`

## Usage

```python
import news_python

news = news_python.Global(key="API-KEY")
news_content = news.get_news(query="bitcoin", source="cnn")

print(f"Title: {news_content.title}\n"
      f"URL: {news_content.url}\n"
      f"Author: {news_content.author}")

```

More can be found in [the docs]() or in the [examples folder](https://github.com/MakufonSkifto/news-python/tree/main/examples)

## Errors

The module will raise `KeyError` if the API can't find anything about the searched topic or country
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

print(f"{news_content.title}\n"
      f"{news_content.url}\n"
      f"{news_content.author}")
```

More can be found in [the docs]() or the [examples folder](https://github.com/MakufonSkifto/news-python/tree/main/examples)

## Errors

The module will raise `KeyError` if the country doesn't exist in the API <b>(Only for the class `Country`)</b>
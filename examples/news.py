import news_python

news = news_python.Global(key="API-KEY")
news_content = news.get_news(country="us", category="technology")

print(news_content.url)

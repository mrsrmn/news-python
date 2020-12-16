import news_python

news = news_python.Global(key="API-KEY")
news_content = news.get_news(query="bitcoin", source="cnn")

print(news_content.url)

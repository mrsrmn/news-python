import news_python

news = news_python.Global(key="API-KEY")
news_content = news.get_news(query="bitcoin", source="cnn")

print(f"{news_content.title}\n"
      f"{news_content.url}\n"
      f"{news_content.author}")

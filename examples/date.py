import news_python

news = news_python.Global(key="API-KEY")
news_content = news.get_by_date(query="bitcoin", frm="2020 11 17")

print(news_content.url)
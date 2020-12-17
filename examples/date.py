import news_python

news = news_python.Global(key="API-KEY")
news_content = news.get_by_date(query="bitcoin", frm="2020 11 17", to="2020 12 17")

print(f"{news_content.title}\n"
      f"{news_content.url}\n"
      f"{news_content.author}")

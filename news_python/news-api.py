class News:
    def __init__(self, status, total_results, publisher_name, author, title, description, url, url_to_image,
                 published_at, content):

        self.status = status
        self.total_results = total_results
        self.publisher_name = publisher_name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.url_to_image = url_to_image
        self.published_at = published_at
        self.content = content

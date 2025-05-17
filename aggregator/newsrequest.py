import requests

# Uses NewsAPI 
# Currently only uses the Everything Endpoint.

class Request:
    def __init__(self, api_key, **args):
        self.api_key = api_key
        self.query = args.get("query")
        self.searchIn = args.get("searchIn")
        self.source = args.get("searchIN")
        self.domains = args.get("domains")
        self.excludeDomains = args.get("excludeDomains")
        self._from = args.get("from")
        self.to = args.get("to")
        self.languague = args.get("language") # 2 Letter ISO-639-1 code
        self.sortBy = args.get("sortBy")
        self.pageSize = args.get("pageSize")
        self.page = args.get("page")

    def send_request(self):
        pass

class Response:
    def __init__(self, response):
        self.status = response.get("status")
        self.totalResults = response.get("totalResult")
        self.articles = []
        for article in response.get("article"):
            self.articles.append(Article(article))

    def __str__(self):
        pass

class Article:
    def __init__(self, article):
        self.source = article.get("source")
        self.author = article.get("author")
        self.title = article.get("title")
        self.description = article.get("description")
        self.url = article.get("url")
        self.urlToImage = article.get("urlToImage")
        self.publishedAt = article.get("publishedAt")
        self.content = article.get("content")

    def __str__(self):
        pass

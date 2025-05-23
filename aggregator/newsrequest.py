from csv import Error
import requests

# Uses NewsAPI 
# Currently only uses the Everything Endpoint.
# TODO: Add representation of Error Response.

class Request:
    def __init__(self, apikey, **args):
        self.apikey = apikey
        self.q = args.get("query")
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

    def __build_request(self):
        res = "https://newsapi.org/v2/everything?"
        params = "&".join([k+"="+v for k, v in self.__dict__.items() if v != None])
        res += params
        return res

    # TODO: Differenciate between OK and Error response. 
    def send_request(self):
        request = self.__build_request()
        response = Response(requests.get(request).json())
        return response


class Response:
    def __init__(self, response):
        self.status = response.get("status")
        if self.status == "error":
            raise ResponseException("error",  response.get("code", response.get("message")))
        
        self.totalResults = response.get("totalResults")
        
        self.articles = []
        found_articles = response.get("articles")
        if found_articles:
            for article in found_articles:
                self.articles.append(Article(article))

    def __str__(self):
        return str(self.__dict__)

class ResponseException(Exception):
    def __init__(self, status, code, message):
        super().__init__(message)
        self.status = status
        self.code = code
    
    def __str__(self):
        return self.message + "\nStatus: " + self.status + ", Code: " + self.code 

class Article:
    def __init__(self, article):
        self.source = article.get("source")
        self.author = article.get("author")
        self.title = article.get("title")
        self.description = article.get("description")
        self.url = article.get("url")
        self.urlToImage = article.get("urlToImage")
        self.publishedAt = article.get("publishedAt")
        self.content = article.get("content") # Requires full API access to view. 

    def __str__(self):
        s = ""
        s += "Source: " + str(self.source["id"]) + ", " + str(self.source["name"]) + "\n"
        s += "Author: " + str(self.author) + "\nTitle: " + str(self.title) + "\n"
        s += "Description: " + str(self.description) + "\n"
        s += "URL: " + str(self.url) + "\nURL to Image: " + str(self.urlToImage) + "\n"
        s += "Published At: " + str(self.publishedAt) #+ "\nContent: " + self.content + "\n"
        return s 

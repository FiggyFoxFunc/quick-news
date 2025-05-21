import json

import click

from aggregator.newsrequest import Request

# TODO: Implement the basic CLI for making queries to the api.

# Setup

with open("secrets.json", "r") as f:
    SECRETS = json.loads(f.read()) 


#req = Request(
#    SECRETS["NewsAPI"], 
#    query="US", 
#    _from="2025-05-21",
#    sortBy="popularity")

#res = req.send_request()

#for article in res.articles:
#    print(article)

#print(res.totalResults)

# CLI Parsing and Request Handling
@click.command
def query():
    pass 

if __name__ == "__main__":
    query()


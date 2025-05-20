import json

import click

from aggregator.newsrequest import Request

# TODO: Implement the basic CLI for making queries to the api.

# Setup

with open("secrets.json", "r") as f:
    SECRETS = json.loads(f.read()) 


#req = Request(
#    SECRETS["NewsAPI"], 
#    query="Apple", 
#    _from="2025-05-19",
#    sortBy="popularity")

#res = req.send_request()
#print(res)

# CLI Parsing and Request Handling
@click.command
def query():
    pass 

if __name__ == "__main__":
    query()


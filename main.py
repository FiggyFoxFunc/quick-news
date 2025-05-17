import click

import json

from aggregator.newsrequest import Request

# Setup

with open("secrets.json", "r") as f:
    SECRETS = json.loads(f.read()) 
req = Request(SECRETS["NewsAPI"])


# CLI Parsing and Request Handling
@click.command
def query():
    pass 

if __name__ == "__main__":
    query()


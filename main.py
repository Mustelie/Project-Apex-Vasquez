import plotly
import sqlite3
import json 
import requests
import api_keys

topHeadlinesEndpoints = "/v2/top-headlines?"
EverythingEndpoints = "/v2/everything?"
baseURL = "https://newsapi.org"
newyorktimesID = "the-new-york-times" 


def EverythingParams(query, website):
    parameter= {
    "apiKey": api_keys.newsAPIKey,
    "q": query,
    "sources":  website, #make sure the input is in id format for the newspai key 
    "sortBy": "publishedAt",
    "pageSize": 100
    }
    return parameter

def getEverything(dictofparams):
    responses = requests.get(baseURL+EverythingEndpoints, params = dictofparams)
    everything = json.loads(responses.text)
    return everything
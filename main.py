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
    "apiKey": "53e7d35bbc77439d87c20bd7b542cbb7",
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
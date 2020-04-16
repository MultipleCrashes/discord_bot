import config as cfg
import requests
import json

def google_search_api(keyword='nodejs'):
    # Google search API
    uri = cfg.QUERY_ENGINE + keyword
    print('query uri', uri)
    search_result = requests.Session().get(uri)
    print('Search result from google : ', search_result.text)
    return search_result.text

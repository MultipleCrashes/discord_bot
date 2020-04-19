import config as cfg
import requests
import json
from googleapiclient.discovery import build


def google_search_api(keyword='nodejs'):
    google_api_key = cfg.GOOGLE_API_KEY
    google_cse_id = cfg.GOOGLE_SEARCH_ID
    service = build("customsearch",
                    "v1",
                    developerKey=google_api_key)
    res = service.cse().list(q=keyword,
                             cx=google_cse_id
                             ).execute()
    print(res['items'])
    return res['items']


google_search_api()
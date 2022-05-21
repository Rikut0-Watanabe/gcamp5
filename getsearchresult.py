import json
from googleapiclient.discovery import build

CUSTOM_SEARCH_ENGINE_ID = "6e65c67507ca027b1"
API_KEY = "<script async src="https://cse.google.com/cse.js?cx=6e65c67507ca027b1"></script><div class="gcse-search"></div>"

def get_search_results(query):
    search = build(
        "customsearch",
        "v1",
        developerkey = API_KEY
    )

    result = search.cse().list(
        q = query,
        cx = CUSTOM_SEARCH_ENGINE_ID,
        lr = 'lang_ja'
        num = 10,
        start = 1
    ).execute()
    return result
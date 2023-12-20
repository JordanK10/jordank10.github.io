import json
import os
import webbrowser

import urllib3

api_url="https://www.balldontlie.io/api/v1/stats"

def use_urllib3(api_url):

    http = urllib3.PoolManager()
    response = http.request('GET', api_url)
    json_response =  response.json()
    print(json_response.keys)
    

    return

use_urllib3(api_url)

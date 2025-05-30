import json

import requests

from api import API_Endpoints


class Utils:
    def get_steam_time():
        json_data = requests.post(API_Endpoints.TWO_FACTOR_TIME_QUERY, data="steamid=1").content
        return int(json.loads(json_data)['response']['server_time'])
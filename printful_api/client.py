from typing import Optional, Dict
import requests
from rich import print
from .constants import USER_AGENT
from .exceptions import InvalidResponse, PrintfulApiException


class PrintfulAPI:
    key: str
    url = 'https://api.printful.com/'

    def __init__(self, key: Optional[str] = None, response_format: str = 'json'):
        # TODO [research] I suppose some End points work without API Key. will dig about it later
        assert not key or len(key) >= 32, 'Invalid Printful store key!'
        self.key = key
        self.response_format = response_format

        self.session = requests.Session()
        self.session.headers['User-Agent'] = USER_AGENT

    def get(self, path, params: Optional[Dict] = None):
        params = params or {}

        return self.request('GET', path, params)

    def request(self, method: str, path: str, params: Optional[Dict] = None, data: Optional[Dict] = None):
        params = params or {}
        data = data or {}

        username, password = self.key.split(':')

        resp = self.session.request(method, self.url + path.lstrip('/'), auth=(username, password), data=data, params=params)
        try:
            resp_json = resp.json()
        except:
            raise InvalidResponse

        if any(k not in resp_json for k in ['code', 'result']):
            raise InvalidResponse('Invalid API response')

        status = resp_json['code']

        if status < 200 or status >= 300:
            raise PrintfulApiException('Unexpected status code: {}'.format(status))

        return resp_json

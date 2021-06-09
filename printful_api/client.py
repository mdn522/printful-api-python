from typing import Optional, Dict
import requests
from rich import print
from .constants import USER_AGENT
from .exceptions import InvalidResponse, PrintfulApiException, PrintfulException


class PrintfulAPI:
    key: str
    url = 'https://api.printful.com/'

    def __init__(self, key: str, response_format: str = 'json'):
        if len(key) < 32:
            raise Exception('Invalid Printful store key!')
        self.key = key
        self.response_format = response_format

        self.session = requests.Session()
        self.session.headers['User-Agent'] = USER_AGENT

    def get(self, path: str, params: Optional[Dict] = None):
        return self.request('GET', path, params)

    def post(self, path: str, params: Optional[Dict] = None, data: Optional[Dict] = None):
        return self.request('POST', path, params=params, data=data)

    def delete(self, path: str, params: Optional[Dict] = None):
        return self.request('DELETE', path, params)

    def put(self, path: str, params: Optional[Dict] = None, data: Optional[Dict] = None):
        return self.request('PUT', path, params=params, data=data)

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

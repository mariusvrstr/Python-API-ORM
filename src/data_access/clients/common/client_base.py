from abc import ABC

import base64
import requests
import json

class ClientBase(ABC):
    base_url = None
    json_data = None
    headers = dict()

    def __init__(self, base_url) -> None:
        self.base_url = base_url

    def set_payload(self, json_data):
        # Check if it is string or json (Convert using json.dumps)
        # Verify that string is valid using json.loads(json_string)
        self.json_data = json.dumps(json_data)

        return self

    def add_header(self, header, value):
        self.headers[header] = value

    def add_basic_auth(self, username, password):
        message_bytes = f'{username}:{password}'.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        self.add_header('Authorization',f'Basic {base64_message}')

    
    def get(self, operation_url = ''):
        url = f'{self.base_url}/{operation_url}'
        response = requests.request("GET", url, headers=self.headers)
        return response


    def post(self, operation_url = ''):
        url = f'{self.base_url}/{operation_url}'
        print(f'Calling {url}...')
        response = requests.request("POST", url, headers=self.headers, data=self.json_data)
        print (f'Response received status [{response.status_code}]')
        return response





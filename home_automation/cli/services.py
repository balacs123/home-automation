import requests
import json
from cli.contants import *


class AutomationRequestHandler():
    def __init__(self, app_data):
        self._app_data = app_data

    def handle_request(self):
        service = self._app_data['service']
        if service == "get_device":
            self.get_device()
        elif service == "add_device":
            self.add_device()
        elif service == 'delete_device':
            self.delete_device()
        elif service == 'update_device':
            self.update_device()
        elif service == 'update_status':
            self.upate_status()

    def add_device(self):
        url = BASE_URL + "/device/"
        result = requests.post(url=url, data=json.dumps(self._app_data), headers=HEADER)
        print(result.text)

    def get_device(self):
        url = BASE_URL + "/device/"
        result = requests.get(url=url, headers=HEADER)
        print(result.text)

    def delete_device(self):
        url = BASE_URL + "/device/" + self._app_data['device_id']
        result = requests.delete(url=url)
        print(result.text)

    def update_device(self):
        url = BASE_URL + "/device/" + self._app_data['device_id']
        print(url)
        result = requests.put(url=url, data=json.dumps(self._app_data), headers=HEADER)
        print(result.text)

    def upate_status(self):
        url = BASE_URL + "/device/status/" + self._app_data['device_id']
        result = requests.put(url=url, data=json.dumps(self._app_data), headers=HEADER)
        print(result.text)




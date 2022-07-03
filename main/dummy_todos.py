import requests
import json

from config import BASE_URL
from tests.data.payload import update_payload, create_payload
from tests.data.headers import headers


class DummyTodos:
    def __init__(self):
        self.base_url = BASE_URL

    def create_todo(self, payload):
        return requests.post(self.base_url + 'add', data=payload, headers=headers)

    def get_all_todos(self):
        return requests.get(self.base_url)

    def get_todo_by_id(self, todo_id):
        return requests.get(self.base_url + todo_id)

    def update_todo_by_id(self, todo_id, payload):
        return requests.put(self.base_url + todo_id, data=payload, headers=headers)

    def delete_todo_by_id(self, todo_id):
        return requests.delete(self.base_url + todo_id)

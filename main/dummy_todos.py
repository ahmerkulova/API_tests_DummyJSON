import requests
import json

from config import BASE_URL, TODO_DEFAULT_ID
from tests.data.payload import update_payload
from tests.data.headers import headers


class DummyTodos:
    def __init__(self):
        self.base_url = BASE_URL
        self.id = TODO_DEFAULT_ID

    def get_all_todos(self):
        return requests.get(self.base_url)

    def get_todo_by_id(self, id):
        return requests.get(self.base_url + id)

    def update_todo_by_id(self, id):
        payload = json.dumps(update_payload)
        return requests.put(self.base_url + self.id, data=payload, headers=headers)

    def delete_todo_by_id(self, id):
        pass

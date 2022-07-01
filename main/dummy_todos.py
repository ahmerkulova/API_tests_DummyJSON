import requests
import json
from cerberus import Validator

from config import BASE_URL, todo_id


class DummyTodos:
    def __init__(self):
        self.base_url = BASE_URL
        self.id = todo_id

    def get_all_todos(self):
        return requests.get(self.base_url)

    def get_todo_by_id(self):
        return requests.get(self.base_url + self.id)

    @staticmethod
    def validate_json_schema(response, schema):
        todo = json.loads(response.text)

        v = Validator(schema)
        is_valid = v.validate(todo)
        return is_valid, v.errors

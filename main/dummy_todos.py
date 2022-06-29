import pytest
import requests

BASE_URL = 'https://dummyjson.com/todos'


class DummyTodos:
    def __init__(self):
        self.base_url = BASE_URL

    def get_all_todos(self):
        return requests.get(self.base_url)

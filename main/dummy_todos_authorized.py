import requests

from main.dummy_todos import DummyTodos
from config import AUTH_URL
from tests.data.headers import headers


class DummyTodosAuthorized(DummyTodos):
    def __init__(self):
        super().__init__()

        self.auth_url = AUTH_URL

    def login_to_get_token(self, payload):
        return requests.post(self.auth_url, data=payload, headers=headers)

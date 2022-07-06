import pytest
from assertpy import assert_that

from tests.data.payload import auth_payload
from main.dummy_todos_authorized import DummyTodosAuthorized
from main.help_functions import *

user = DummyTodosAuthorized()


@pytest.mark.auth_user
class TestUserTodos:
    @pytest.fixture(scope='function', autouse=True)
    def save_token(self, payload=auth_payload):
        response = user.login_to_get_token(deserialized(payload))
        token = serialized(response)['token']
        auth_headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        return auth_headers

    def test_user_can_get_all_todos(self, headers=self.auth_headers):
        pass



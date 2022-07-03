from assertpy import assert_that

from main.dummy_todos import DummyTodos
from main.help_functions import *
from tests.data.payload import *
from config import TODOS_TOTAL

todos = DummyTodos()


@pytest.mark.smoke
def test_guest_can_create_todo():
    response = todos.create_todo(deserialized(create_payload))
    assert_that(response.text).is_not_empty()
    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.smoke
def test_created_todo_has_expected_fields():
    response = todos.create_todo(deserialized(create_payload))
    body = serialized(response)
    assert_that(body).has_todo(CREATE_TODO)
    assert_that(body).has_completed(CREATE_STATUS)
    assert_that(body).has_userId(CREATE_USERID)


def test_created_todo_has_unique_id(unique_id=TODOS_TOTAL + 1):
    response = todos.create_todo()
    body = serialized(response)
    assert_that(body).has_id(unique_id)

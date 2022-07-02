from assertpy import assert_that

from main.dummy_todos import DummyTodos
from main.help_functions import *
from tests.data.payload import *

todos = DummyTodos()


def test_todo_can_be_updated_by_id():
    response = todos.update_todo_by_id(id)
    assert_that(response.text).is_not_empty()
    assert_that(response.status_code).is_equal_to(200)


def test_all_attributes_are_updated_correctly():
    response = todos.update_todo_by_id(id)
    body = json.loads(response.text)
    assert_that(body).has_todo(UPDATE_TODO)
    assert_that(body).has_completed(UPDATE_STATUS)
    assert_that(body).has_userId(UPDATE_USERID)


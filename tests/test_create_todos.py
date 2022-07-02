from assertpy import assert_that

from main.dummy_todos import DummyTodos
from main.help_functions import *
from tests.data.payload import *
from config import TODOS_TOTAL

todos = DummyTodos()


def test_todo_can_be_created():
    response = todos.create_todo()
    assert_that(response.text).is_not_empty()
    assert_that(response.status_code).is_equal_to(200)


def test_created_todo_has_correct_attributes():
    response = todos.create_todo()
    body = json.loads(response.text)
    assert_that(body).has_todo(CREATE_TODO)
    assert_that(body).has_completed(CREATE_STATUS)
    assert_that(body).has_userId(CREATE_USERID)


def test_created_todo_has_unique_id(unique_id=TODOS_TOTAL + 1):
    response = todos.create_todo()
    body = json.loads(response.text)
    assert_that(body).has_id(unique_id)

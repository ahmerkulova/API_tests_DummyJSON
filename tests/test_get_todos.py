from assertpy import assert_that

from main.dummy_todos import DummyTodos
from tests.data.schemas import *

todos = DummyTodos()


def test_get_all_todos():
    response = todos.get_all_todos()
    assert_that(response.status_code).is_equal_to(200)


def test_get_todo_by_id():
    response = todos.get_todo_by_id()
    assert_that(response.status_code).is_equal_to(200)


def test_todo_by_id_has_expected_schema():
    response = todos.get_todo_by_id()
    is_valid, errors = todos.validate_json_schema(response, todo_id_schema)
    assert_that(is_valid).described_as(errors).is_true()

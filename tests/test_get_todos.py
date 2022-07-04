import pytest
from assertpy import assert_that

from main.dummy_todos import DummyTodos
from main.help_functions import *
from tests.data.schemas import schema_todo_id
from config import TODOS_RANGE, TODOS_INVALID_TYPE

todos = DummyTodos()


@pytest.mark.smoke
def test_guest_can_get_all_todos():
    response = todos.get_all_todos()
    assert_that(response.text).is_not_empty()
    assert_that(response.status_code).is_equal_to(200)


def test_all_todos_total_is_correct(correct_total=max(TODOS_RANGE)):
    response = todos.get_all_todos()
    all_todos = serialized(response)
    assert_that(all_todos).has_total(correct_total)


@pytest.mark.smoke
def test_guest_can_get_todo_by_id(id=get_random_id()):
    response = todos.get_todo_by_id(id)
    assert_that(response.text).is_not_empty()
    assert_that(response.status_code).is_equal_to(200)


def test_todo_by_id_has_expected_schema(id=get_random_id()):
    response = todos.get_todo_by_id(id)
    is_valid, errors = validate_json_schema(response, schema_todo_id)
    assert_that(is_valid).described_as(errors).is_true()


@pytest.mark.negative
@pytest.mark.parametrize('id', get_boundaries())
def test_guest_cant_get_todo_by_id_out_of_range(id):
    response = todos.get_todo_by_id(id)
    body = serialized(response)
    assert_that(response.status_code).is_equal_to(404)
    assert_that(body).contains_value(f"Todo with id '{id}' not found")


@pytest.mark.negative
@pytest.mark.parametrize('id', [id for id in TODOS_INVALID_TYPE])
def test_guest_cant_get_todo_by_invalid_id_type(id):
    response = todos.get_todo_by_id(id)
    body = serialized(response)
    assert_that(response.status_code).is_equal_to(404)
    assert_that(body).contains_value(f"Todo with id '{id}' not found")

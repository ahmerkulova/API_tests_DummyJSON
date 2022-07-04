import pytest
from assertpy import assert_that

from main.dummy_todos import DummyTodos
from main.help_functions import *
from tests.data.payload import *

todos = DummyTodos()


@pytest.mark.smoke
def test_guest_can_update_todo_by_id(id=get_random_id(), payload=update_payload):
    response = todos.update_todo_by_id(id, deserialized(payload))
    assert_that(response.text).is_not_empty()
    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.smoke
def test_all_updated_fields_are_correct(id=get_random_id(), payload=update_payload):
    response = todos.update_todo_by_id(id, deserialized(payload))
    body = serialized(response)
    assert_that(body).has_todo(UPDATE_TODO)
    assert_that(body).has_completed(UPDATE_STATUS)
    assert_that(body).has_userId(UPDATE_USERID)


@pytest.mark.negative
def test_guest_cant_update_todo_with_unexpected_parameter(id=get_random_id(), payload=update_payload_new_parameter):
    response = todos.update_todo_by_id(id, deserialized(payload))
    body = serialized(response)
    assert_that(body).does_not_contain_value(UPDATE_NEW_PARAMETER)


@pytest.mark.negative
@pytest.mark.parametrize('id', get_boundaries())
def test_guest_cant_update_todo_out_of_range(id, payload=update_payload):
    response = todos.update_todo_by_id(id, deserialized(payload))
    body = serialized(response)
    assert_that(response.status_code).is_equal_to(404)
    assert_that(body).contains_value(f"Todo with id '{id}' not found")

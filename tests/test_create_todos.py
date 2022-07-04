import pytest
from assertpy import assert_that

from main.dummy_todos import DummyTodos
from main.help_functions import *
from tests.data.payload import *
from config import TODOS_RANGE

todos = DummyTodos()


@pytest.mark.smoke
def test_guest_can_create_todo(payload=create_payload):
    response = todos.create_todo(deserialized(payload))
    assert_that(response.text).is_not_empty()
    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.smoke
def test_created_todo_has_expected_fields(payload=create_payload):
    response = todos.create_todo(deserialized(payload))
    body = serialized(response)
    assert_that(body).has_todo(CREATE_TODO)
    assert_that(body).has_completed(CREATE_STATUS)
    assert_that(body).has_userId(CREATE_USERID)


def test_created_todo_has_unique_id(payload=create_payload, unique_id=max(TODOS_RANGE) + 1):
    response = todos.create_todo(deserialized(payload))
    body = serialized(response)
    assert_that(body).has_id(unique_id)


@pytest.mark.negative
@pytest.mark.parametrize('payload', (empty_payload, payload_wo_userId))
def test_guest_cant_create_todo_without_userId(payload):
    response = todos.create_todo(deserialized(payload))
    body = serialized(response)
    assert_that(response.status_code).is_equal_to(400)
    assert_that(body).has_message('User id is required')


@pytest.mark.negative
def test_guest_cant_create_todo_with_incorrect_userId_type(payload=payload_incorrect_userId):
    response = todos.create_todo(deserialized(payload))
    body = serialized(response)
    assert_that(response.status_code).is_equal_to(400)
    assert_that(body).contains_value(f"Invalid user id '{CREATE_INVALID_USERID}'")

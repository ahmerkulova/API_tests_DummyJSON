from assertpy import assert_that

from main.dummy_todos import DummyTodos
from main.help_functions import *
from tests.data.schemas import schema_deleted_todo
from config import *

todos = DummyTodos()


@pytest.mark.smoke
def test_guest_can_delete_todo_by_id(id='99'):
    response = todos.delete_todo_by_id(id)
    deletion_response = serialized(response)
    assert_that(response.text).is_not_empty()
    assert_that(response.status_code).is_equal_to(200)
    assert_that(deletion_response).has_isDeleted(True)


def test_deleted_todo_has_expected_schema(id=TODO_ID):
    response = todos.delete_todo_by_id(id)
    is_valid, errors = validate_json_schema(response, schema_deleted_todo)
    assert_that(is_valid).described_as(errors).is_true()


@pytest.mark.negative
@pytest.mark.parametrize('id', ('0', str(TODOS_TOTAL + 1)))
def test_guest_cant_delete_todo_out_of_range(id):
    response = todos.delete_todo_by_id(id)
    body = serialized(response)
    assert_that(response.status_code).is_equal_to(404)
    assert_that(body).contains_value(f"Todo with id '{id}' not found")


@pytest.mark.negative
@pytest.mark.parametrize('id', ('3.14', 'True'))
def test_guest_cant_delete_todo_by_invalid_id_type(id):
    response = todos.delete_todo_by_id(id)
    body = serialized(response)
    assert_that(response.status_code).is_equal_to(404)
    assert_that(body).contains_value(f"Todo with id '{id}' not found")

from assertpy import assert_that

from main.dummy_todos import DummyTodos
from main.help_functions import *
from tests.data.schemas import schema_deleted_todo

todos = DummyTodos()


@pytest.mark.smoke
def test_guest_can_delete_todo_by_id(id='99'):
    response = todos.delete_todo_by_id(id)
    deletion_response = serialized(response)
    assert_that(response.text).is_not_empty()
    assert_that(response.status_code).is_equal_to(200)
    assert_that(deletion_response).has_isDeleted(True)


def test_deleted_todo_has_expected_schema():
    response = todos.delete_todo_by_id(id)
    is_valid, errors = validate_json_schema(response, schema_deleted_todo)
    assert_that(is_valid).described_as(errors).is_true()

from assertpy import assert_that

from main.dummy_todos import DummyTodos
from main.help_functions import *
from tests.data.payload import *
from config import TODO_ID

todos = DummyTodos()


@pytest.mark.smoke
def test_guest_can_update_todo_by_id(id=TODO_ID):
    response = todos.update_todo_by_id(id, deserialized(update_payload))
    assert_that(response.text).is_not_empty()
    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.smoke
def test_all_updated_fields_are_correct(id=TODO_ID):
    response = todos.update_todo_by_id(id, deserialized(update_payload))
    body = serialized(response)
    assert_that(body).has_todo(UPDATE_TODO)
    assert_that(body).has_completed(UPDATE_STATUS)
    assert_that(body).has_userId(UPDATE_USERID)

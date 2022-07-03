from assertpy import assert_that

from main.dummy_todos import DummyTodos
from main.help_functions import *
from tests.data.payload import *

todos = DummyTodos()


@pytest.mark.smoke
def test_guest_can_update_todo_by_id():
    response = todos.update_todo_by_id(id)
    assert_that(response.text).is_not_empty()
    assert_that(response.status_code).is_equal_to(200)


@pytest.mark.smoke
def test_all_updated_fields_are_correct():
    response = todos.update_todo_by_id(id)
    body = serialized(response)
    assert_that(body).has_todo(UPDATE_TODO)
    assert_that(body).has_completed(UPDATE_STATUS)
    assert_that(body).has_userId(UPDATE_USERID)


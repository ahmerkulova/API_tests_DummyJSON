from assertpy import assert_that

from main.dummy_todos import DummyTodos
from main.help_functions import *
from tests.data.schemas import schema_todo_id
from config import TODOS_TOTAL

todos = DummyTodos()


@pytest.mark.smoke
def test_guest_can_get_all_todos():
    response = todos.get_all_todos()
    assert_that(response.text).is_not_empty()
    assert_that(response.status_code).is_equal_to(200)


def test_all_todos_total_is_correct(correct_total=TODOS_TOTAL):
    response = todos.get_all_todos()
    all_todos = json.loads(response.text)
    assert_that(all_todos).has_total(correct_total)


@pytest.mark.smoke
def test_guest_can_get_todo_by_id(id='13'):
    response = todos.get_todo_by_id(id)
    assert_that(response.text).is_not_empty()
    assert_that(response.status_code).is_equal_to(200)


def test_todo_by_id_has_expected_schema():
    response = todos.get_todo_by_id(todos.id)
    is_valid, errors = validate_json_schema(response, schema_todo_id)
    assert_that(is_valid).described_as(errors).is_true()

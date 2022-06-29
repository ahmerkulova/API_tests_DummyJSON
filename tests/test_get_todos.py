from main.dummy_todos import DummyTodos

todos = DummyTodos()


def test_get_all_todos():
    response = todos.get_all_todos()
    assert response.status_code == 200, f'Status code is {response.status_code}, should be 200'


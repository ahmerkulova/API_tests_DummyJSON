## Sample testing framework for DummyJSON API (basic CRUD requests) 
### DummyJSON documentation can be checked [here](https://dummyjson.com/docs)

### Stack
- Python 3.10.2
- Pytest 7.1.2
- Main python packages used: requests, cerberus, assertpy

### Setting environment (Windows 10)
- Make sure there's proper Python version installed (otherwise get it on the official site)
```
python --version
```
- Clone the repository to the target folder
```
cd projectfolder
git clone git@github.com:ahmerkulova/API_tests_DummyJSON.git
```
- Install packages from Pipfile, create and run new virtual environment
```
pipenv install
pipenv shell
```
To deactivate virtual environment use the following command:
```
exit
```

### Running tests
- To run all the tests
```
pytest -v --tb=line
```
- To run specified tests (example):
```
pytest -v --tb=line tests/test_create_todos.py::test_guest_can_create_todo
```
- To run tests with a certain mark (example):
```
pytest -vm smoke
```
- To run all tests in parallel (fastest way):
```
pytest -v -n auto
```
User marks are specified in pytest.ini

### Getting Allure report
- Make sure there's Allure installed (otherwise use 'pipenv install allure-pytest' and then get zip package installed from the official site)
```
allure --version
```
- Generate a new subfolder for reports in the project directory
```
cd projectfolder
allure generate
```
- Run tests specifying reports folder
```
pytest --alluredir=allure-report/
```
- Finally check the report in the default browser
```
allure serve allure-report/
```
Ctrl+C is to get back to virtual environment
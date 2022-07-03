import pytest
import json
from cerberus import Validator


def validate_json_schema(response, schema):
    todo = json.loads(response.text)
    v = Validator(schema)
    is_valid = v.validate(todo)
    return is_valid, v.errors

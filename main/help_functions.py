import json
from cerberus import Validator
from random import randint

from config import TODOS_RANGE


def deserialized(payload):
    return json.dumps(payload)


def get_boundaries():
    return str(min(TODOS_RANGE) - 1), str(max(TODOS_RANGE) + 1)


def get_random_id():
    return str(randint(min(TODOS_RANGE), max(TODOS_RANGE)))


def serialized(response):
    return json.loads(response.text)


def validate_json_schema(response, schema):
    todo = json.loads(response.text)
    v = Validator(schema)
    is_valid = v.validate(todo)
    return is_valid, v.errors


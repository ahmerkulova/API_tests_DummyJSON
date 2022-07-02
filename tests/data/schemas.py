schema_todo_id = {
    "id": {'type': 'integer'},
    "todo": {'type': 'string'},
    "completed": {'type': 'boolean'},
    "userId": {'type': 'integer'}
}

deletion_datetime_regex = '^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9])' \
                          r':([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'

schema_deleted_todo = {
    "id": {'type': 'integer'},
    "todo": {'type': 'string'},
    "completed": {'type': 'boolean'},
    "userId": {'type': 'integer'},
    "isDeleted": {'type': 'boolean'},
    "deletedOn": {'type': 'string', 'regex': deletion_datetime_regex}
}

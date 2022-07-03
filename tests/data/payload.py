UPDATE_TODO = "Lay down your arms, give up the fight"
UPDATE_STATUS = False
UPDATE_USERID = 21

update_payload = {
    "todo": UPDATE_TODO,
    "completed": UPDATE_STATUS,
    "userId": UPDATE_USERID
}

CREATE_TODO = "Imagine there's no heaven"
CREATE_STATUS = True
CREATE_USERID = 12
CREATE_INVALID_USERID = "Hello"

create_payload = {
    "todo": CREATE_TODO,
    "completed": CREATE_STATUS,
    "userId": CREATE_USERID
}

empty_payload = {
}

payload_wo_userId = {
    "todo": CREATE_TODO,
    "completed": CREATE_STATUS,
}

payload_incorrect_userId = {
    "todo": CREATE_TODO,
    "userId": CREATE_INVALID_USERID
}

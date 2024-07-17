from typing import List, Dict
from user_data import users
from commands import Commands
from utils import normalize_phone


def get_response(cmd: str, args: List):
    response = None
    match cmd:
        case Commands.HELLO:
            response = Commands.messages.get(Commands.HELLO)
        case Commands.ADD:
            response = add_contact(args)
        case Commands.CHANGE:
            response = change_contact(args)
        case Commands.PHONE:
            response = show_phone(args)
        case Commands.ALL:
            response = show_all()
    return response


def add_contact(args: List) -> str:
    message = Commands.messages.get(Commands.INVALID)
    if len(args) == 2:
        user_name = args[0]
        phone_num = normalize_phone(args[1])
        if user_name not in users and phone_num:
            users[user_name] = phone_num
            message = Commands.messages.get(Commands.ADD)
    return message


def change_contact(args: List) -> str:
    message = Commands.messages.get(Commands.INVALID)
    if len(args) == 2:
        user_name = args[0]
        phone_num = normalize_phone(args[1])
        if user_name in users and phone_num:
            users[user_name] = phone_num
            message = Commands.messages.get(Commands.CHANGE)
    return message


def show_phone(args: List) -> str:
    message = Commands.messages.get(Commands.INVALID)
    if len(args) == 1:
        message = users.get(args[0])
    return message


def show_all() -> Dict:
    return users

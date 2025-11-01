import os.path
from UserManage.user import User
from Exceptions.register_error import RegisterError
from UserManage.user import Username
from UserManage.password import Password
import json


class Register:
    @classmethod
    def register_user(cls, user: User, filepath="users.json"):
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as file:
                try:
                    users = json.load(file)
                except json.JSONDecodeError:
                    users = []
        else:
            users = []
        username_str = user.username.username

        if username_str in users:
            raise RegisterError("The user already exists")

        users.append(username_str)

        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(users, file, ensure_ascii=False, indent=4)

        return True

    @classmethod
    def set_password(cls, user: User, password: Password, filepath="passwords.json"):
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as file:
                try:
                    passwords = json.load(file)
                except json.JSONDecodeError:
                    passwords = {}
        else:
            passwords = {}

        passwords[user.username.username] = password.get_password_only_for_reg()

        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(passwords, file, ensure_ascii=False, indent=4)

        return True


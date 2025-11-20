import os.path
from UserManage.user import User
from Exceptions.register_error import RegisterError
from UserManage.password import Password
from UserManage.username_validator import UsernameValidator
from Exceptions.invalid_username_error import InvalidUsernameError
import json


class Register:
    """
    Register class
    """
    @classmethod
    def register_user(cls, user: User, filepath="users.json"):
        """
        user register method
        registers the user and puts to file with users
        :param user: User
        :param filepath: "users.json"
        """
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as file:
                try:
                    users = json.load(file)
                except json.JSONDecodeError:
                    users = []
        else:
            users = []
        username_str = user.username
        if not UsernameValidator.is_valid(user.username):
            raise InvalidUsernameError("Invalid username")
        if username_str in users:
            raise RegisterError("The user already exists")

        users.append(username_str)

        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(users, file, ensure_ascii=False, indent=4)

        return True

    @classmethod
    def set_password(cls, user: User, password: Password, filepath="passwords.json"):
        """
        password setter method
        sets password for a user
        :param user: User
        :param password: Password
        :param filepath: "passwords.json"
        :return: password is successfully set
        """
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


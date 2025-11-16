import os
import json

from UserManage.user import User
from UserManage.password import Password

from Exceptions.login_error import LogInError


class LogIn:
    """
    LogIn class

    Helps to log in system
    """

    @classmethod
    def log_in(cls, user: User, password: Password, users_file="users.json", passwords_file="passwords.json"):
        """
        log in method

        :param user: User
        :param password: Password
        :param users_file: "users.json"
        :param passwords_file: "passwords.json"
        """
        if not os.path.exists(users_file):
            raise FileNotFoundError(f"{users_file} not found")

        with open(users_file, "r", encoding="utf-8") as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = []

        if user.username not in users:
            raise LogInError("User does not exist")

        with open(passwords_file, "r", encoding="utf-8") as f:
            try:
                passwords = json.load(f)
            except json.JSONDecodeError:
                passwords = {}

        stored_password = passwords.get(user.username)
        if stored_password is None or stored_password != password.get_password_only_for_reg():
            raise LogInError("Incorrect password")

        return True



import sys
import os
import json
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from UserManage.username import Username
from UserManage.user import User
from UserManage.password import Password
from UserManage.user_profile import UserProfile
from Authentication.register import Register
from Exceptions.register_error import RegisterError
from Exceptions.invalid_username_error import InvalidUsernameError
from MainEntities.date import Date
from Authentication.log_in import LogIn
from Exceptions.login_error import LogInError


@pytest.fixture
def tmp_files(tmp_path):
    users_file = tmp_path / "test_users.json"
    passwords_file = tmp_path / "test_passwords.json"
    return str(users_file), str(passwords_file)


def test_registration(tmp_files):
    users_file, passwords_file = tmp_files
    user = User(Username("test_user1"), UserProfile("bio", Date(2000, 1, 1)))
    assert Register.register_user(user, users_file)


def test_duplicate_registration(tmp_files):
    users_file, _ = tmp_files
    user = User(Username("same_user"), UserProfile("bio", Date(2000, 1, 1)))
    Register.register_user(user, users_file)

    with pytest.raises(RegisterError):
        Register.register_user(user, users_file)


def test_invalid_username(tmp_files):
    users_file, _ = tmp_files
    user = User(Username("a!"), UserProfile("bio", Date(2000, 1, 1)))

    with pytest.raises(InvalidUsernameError):
        Register.register_user(user, users_file)


def test_login_success(tmp_path):
    from UserManage.user_profile import UserProfile
    from UserManage.username import Username
    from MainEntities.date import Date
    from Authentication.log_in import LogIn
    users_file = tmp_path / "users.json"
    passwords_file = tmp_path / "passwords.json"
    username = "testuser"
    password_str = "My_pass_123!"
    users_file.write_text(json.dumps([username], ensure_ascii=False))
    password = Password(password_str)
    passwords_file.write_text(json.dumps({username: password.get_password_only_for_reg()}, ensure_ascii=False))
    user = User(Username(username), UserProfile("bio", Date(2000, 1, 1)))
    assert LogIn.log_in(user, password, str(users_file), str(passwords_file))


def test_login_wrong_password(tmp_path):
    from Exceptions.login_error import LogInError
    users_file = tmp_path / "users.json"
    passwords_file = tmp_path / "passwords.json"
    username = "testuser"
    correct_password = Password("Correct123!")
    wrong_password = Password("Wrong123!")
    users_file.write_text(json.dumps([username], ensure_ascii=False))
    passwords_file.write_text(json.dumps({username: correct_password.get_password_only_for_reg()}))
    user = User(Username(username), UserProfile("bio", Date(2000, 1, 1)))
    with pytest.raises(LogInError):
        LogIn.log_in(user, wrong_password, str(users_file), str(passwords_file))


def test_login_user_not_exist(tmp_path):
    users_file = tmp_path / "users.json"
    passwords_file = tmp_path / "passwords.json"
    users_file.write_text(json.dumps([]))
    passwords_file.write_text(json.dumps({}))
    user = User(Username("ghost"), UserProfile("bio",  Date(2000, 1, 1)))
    password = Password("SomePass123!")
    with pytest.raises(LogInError):
        LogIn.log_in(user, password, str(users_file), str(passwords_file))
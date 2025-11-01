from UserManage.username import Username


class NameValidator:
    def __init__(self, username: Username):
        self.__username = username

    @property
    def username(self):
        return self.__username

    def is_valid(self):
        return (
                3 <= len(self.__username.username) <= 20 and
                self.__username.username.isalnum()
        )

    def equals(self, other: Username):
        return self.__username == other.username

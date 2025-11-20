from UserManage.username import Username


class UsernameValidator:
    """
    Username validator class
    """
    def __init__(self, username: Username):
        """
        Constructor
        :param username: Username
        """
        self.__username = username

    @property
    def username(self):
        return self.__username

    @staticmethod
    def is_valid(username: Username):
        """
        Checks if the username is valid
        :param username: Username
        :return: the username is valid
        """
        allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
        return (
            3 <= len(str(username)) <= 20
            and all(c in allowed for c in str(username))
        )

    def equals(self, other: Username):
        """
        Compares two usernames
        :param other: Username to compare
        :return: username is equal to other username
        """
        return self.__username.username == other.username

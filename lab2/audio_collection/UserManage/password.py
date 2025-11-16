from Exceptions.weak_password_error import WeakPasswordError


class Password:
    """
    Password class
    """
    def __init__(self, password: str):
        """
        Constructor
        :param password: password as str
        """
        if not self.__is_strong(password):
            raise WeakPasswordError("The password is too weak")
        self.__password = password

    @staticmethod
    def __is_strong(password: str):
        """
        Checks if password is strong enough
        :param password: password as str
        :return: password is strong
        """
        has_digit = any(i.isdigit() for i in password)
        has_lower = any(i.islower() for i in password)
        has_special_symbol = any(i in "!@#$%^&*()?><:;" for i in password)
        return len(password) >= 8 and has_lower and has_digit and has_special_symbol

    def verify(self, input_password: str):
        """
        Verifies the password
        :param input_password: Password as str
        """
        return self.__password == input_password

    def change(self, old_password: str, new_password: str):
        """
        Changes the password
        :param old_password: Old password
        :param new_password: New password
        """
        if self.verify(old_password) and not self.__is_strong(new_password):
            raise WeakPasswordError("The password is too weak")
        self.__password = new_password

    def __str__(self):
        return '*' * len(self.__password)

    def get_password_only_for_reg(self):
        return self.__password

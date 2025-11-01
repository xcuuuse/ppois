from Exceptions.weak_password_error import WeakPasswordError


class Password:
    def __init__(self, password: str):
        if not self.__is_strong(password):
            raise WeakPasswordError("The password is too weak")
        self.__password = password

    @staticmethod
    def __is_strong(password: str):
        has_digit = any(i.isdigit() for i in password)
        has_lower = any(i.islower() for i in password)
        has_special_symbol = any(i in "!@#$%^&*()?><:;" for i in password)
        return len(password) >= 8 and has_lower and has_digit and has_special_symbol

    def verify(self, input_password: str):
        return self.__password == input_password

    def change(self, old_password: str, new_password: str):
        if self.verify(old_password) and self.__is_strong(new_password):
            self.__password = new_password

    def __str__(self):
        return '*' * len(self.__password)

    def get_password_only_for_reg(self):
        return self.__password

from IdManage.id_generator import IdGenerator


class UserId(IdGenerator):
    """
    User id class
    """
    __user_id = 0

    @classmethod
    def generate_id(cls):
        """
        Generates user id
        :return: user id
        """
        cls.__user_id += 1
        return cls.__user_id

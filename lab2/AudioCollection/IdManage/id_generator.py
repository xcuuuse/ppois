class IdGenerator:
    """
    Id generator base class
    """
    __private_id = 0

    @classmethod
    def generate_id(cls):
        cls.__private_id += 1
        return cls.__private_id


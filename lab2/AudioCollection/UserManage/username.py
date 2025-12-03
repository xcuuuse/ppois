class Username:
    """
    Username class
    """
    def __init__(self, username: str):
        """
        Constructor
        :param username: Username as str
        """
        self.__username = username

    @property
    def username(self):
        return self.__username

    
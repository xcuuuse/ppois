class Genre:
    """
    Genre class
    """
    def __init__(self, genre_name: str):
        """
        Constructor
        :param genre_name: Genre name
        """
        self.__genre_name = genre_name

    @property
    def genre_name(self):
        return self.__genre_name



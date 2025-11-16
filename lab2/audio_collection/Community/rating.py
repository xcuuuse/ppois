class Rating:
    """
    Rating class
    """
    def __init__(self, rating: int):
        """
        Constructor
        :param rating: int
        """
        self.__rating = rating

    def __int__(self):
        return self.__rating


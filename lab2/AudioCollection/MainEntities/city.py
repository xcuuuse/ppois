class City:
    """
    City class
    """
    def __init__(self, city: str):
        """
        Constructor
        :param city: City name
        """
        self.__city = city

    def __str__(self):
        return self.__city

class Musician:
    """
    Musician class
    """
    def __init__(self, name: str):
        """
        Constructor
        :param name: musician name
        """
        self.__name = name
        self.__instruments: list[str] = []
        self.__birth_year: int = 0

    @property
    def name(self):
        return self.__name

    @property
    def instruments(self):
        return self.__instruments

    @property
    def birth_year(self):
        return self.__birth_year

    def get_info(self):
        """
        A method to get info about musician
        :return: musician info
        """
        return\
            f"{self.__name}, born in {self.__birth_year}. {", ".join(str(i.title()) for i in self.__instruments)}\n"

from MainEntities.Artists.artist import Artist


class Label:
    """
    Label class
    """
    def __init__(self, name: str):
        """
        Constructor
        :param name: Label name
        """
        self.__name = name
        self.__country: str = ""
        self.__founded_year: int = 0
        self.__artists: list[Artist] = []

    @property
    def name(self):
        return self.__name

    @property
    def country(self):
        return self.__country

    @property
    def founded_year(self):
        return self.__founded_year

    @property
    def artists(self):
        return [i.name for i in self.__artists]

    def add_artist(self, artist: Artist):
        self.__artists.append(artist)




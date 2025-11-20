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

    def remove_artist(self, artist: Artist):
        """
        Removes an artist from the label if present
        :param artist: Artist instance
        """
        if artist in self.__artists:
            self.__artists.remove(artist)

    def get_artist_info(self):
        """
        Returns information about all artists signed to the label
        :return: list of dicts with artist names and number of albums
        """
        return [{"name": artist.name, "albums_count": len(artist.albums)} for artist in self.__artists]


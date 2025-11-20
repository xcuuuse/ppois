from MainEntities.Artists.artist import Artist
from MainEntities.Artists.musician import Musician
from MainEntities.Albums.album import Album


class Band(Artist):
    """
    Band class
    """
    def __init__(self, name: str, albums: list[Album],
                 musicians: list[Musician]):
        """
        Constructor
        :param name: Band name
        :param albums: Band albums
        :param musicians: Band musicians
        """
        super().__init__(name, albums)
        self.__musicians = musicians

    @property
    def musicians(self):
        return self.__musicians

    def get_members_info(self):
        """
        A method to get members info
        :return: Band members info
        """
        for i in self.__musicians:
            return i.get_info()


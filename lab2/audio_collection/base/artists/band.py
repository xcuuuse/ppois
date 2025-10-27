from base.artists.artist import Artist
from base.artists.musician import Musician
from base.albums.album import Album


class Band(Artist):
    def __init__(self, name: str, albums: list[Album],
                 musicians: list[Musician]):
        super().__init__(name, albums)
        self.__musicians = musicians

    @property
    def musicians(self):
        return self.__musicians

    def get_members_info(self):
        for i in self.__musicians:
            return i.get_info()

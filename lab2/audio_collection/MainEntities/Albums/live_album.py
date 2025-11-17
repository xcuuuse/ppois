from MainEntities.Albums.album import Album
from MainEntities.track import Track
from MainEntities.genre import Genre
from MainEntities.label import Label
from MainEntities.city import City


class LiveAlbum(Album):
    """
    Live album class
    """
    def __init__(self, title: str, tracks: list[Track], genre: Genre, year: int, label: Label,
                 city: City):
        """
        Constructor
        :param title: Live album title
        :param tracks: Live album tracks
        :param genre: Live album genre
        :param year: Live album year
        :param label: Live album label
        :param city: Live album city
        """
        super().__init__(title, tracks, genre, year, label)
        self.__city = city

    @property
    def city(self):
        return self.__city

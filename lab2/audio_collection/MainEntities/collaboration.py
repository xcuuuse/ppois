from MainEntities.track import Track
from MainEntities.genre import Genre
from MainEntities.Artists.artist import Artist


class Collaboration(Track):
    """
    Collaboration class
    """
    def __init__(self, title: str, genre: Genre, artists: list[Artist]):
        """
        Constructor
        :param title: Collaboration title
        :param genre: Collaboration genre
        :param artists: Artists
        """
        super().__init__(title, genre)
        self.__artists = artists

    @property
    def artists(self):
        return self.__artists


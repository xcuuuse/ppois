from MainEntities.Albums.album import Album
from MainEntities.track import Track
from MainEntities.genre import Genre
from MainEntities.label import Label


class Ep(Album):
    """
    Ep class
    """
    def __init__(self, title: str, tracks: list[Track], genre: Genre, year: int,
                 label: Label):
        """
        Constructor
        :param title: Ep title
        :param tracks: Ep tracks
        :param genre: Ep genre
        :param year: Ep year
        :param label: Ep label
        """
        super().__init__(title, tracks, genre, year, label)


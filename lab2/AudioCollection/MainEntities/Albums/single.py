from MainEntities.Albums.album import Album
from MainEntities.track import Track
from MainEntities.genre import Genre
from MainEntities.label import Label


class Single(Album):
    """
    Single(album) class
    """
    def __init__(self, title: str, tracks: list[Track], genre: Genre, year: int,
                 label: Label):
        """
        Constructor
        :param title: Single title
        :param tracks: Single tracks
        :param genre: Single genre
        :param year: Single year
        :param label: Single label
        """
        super().__init__(title, tracks, genre, year, label)



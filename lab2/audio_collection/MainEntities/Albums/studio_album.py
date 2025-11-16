from MainEntities.track import Track
from MainEntities.genre import Genre
from MainEntities.label import Label
from MainEntities.Albums.album import Album


class StudioAlbum(Album):
    """
    Studio album class
    """
    def __init__(self, title: str, tracks: list[Track], genre: Genre, year: int,
                 label: Label):
        """
        Constructor
        :param title: Studio album title
        :param tracks: Studio album tracks
        :param genre: Studio album genre
        :param year: Studio album year
        :param label: Studio album label
        """
        super().__init__(title, tracks, genre, year, label)


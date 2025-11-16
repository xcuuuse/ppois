from MainEntities.track import Track
from MainEntities.genre import Genre
from MainEntities.Artists.artist import Artist
from MainEntities.duration import Duration


class Cover(Track):
    """
    Cover class
    """
    def __init__(self, title: str, genre: Genre, cover_author: Artist):
        """
        Constructor
        :param title: Cover title
        :param genre: Cover genre
        :param cover_author: Cover author
        """
        super().__init__(title, genre)
        self.__cover_author = cover_author

    @property
    def cover_author(self):
        return self.__cover_author

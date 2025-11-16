from MainEntities.track import Track
from MainEntities.genre import Genre
from MainEntities.Artists.artist import Artist


class Remix(Track):
    """
    Remix class
    """
    def __init__(self, title: str, genre: Genre, author: Artist):
        """
        Constructor
        :param title: Remix title
        :param genre: Remix genre
        :param author: Remix author
        """
        super().__init__(title, genre)
        self.__author = author

    @property
    def author(self):
        return self.__author


from Base.Albums.album import Album
from Base.track import Track
from Base.genre import Genre


class LiveAlbum(Album):
    def __init__(self, title: str, tracks: list[Track], genre: Genre, year: int,
                 city: str):
        super().__init__(title, tracks, genre, year)
        self.__city = city

    @property
    def label(self):
        return self.__city



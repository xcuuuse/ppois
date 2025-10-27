from base.albums.album import Album
from base.track import Track
from base.genre import Genre


class StudioAlbum(Album):
    def __init__(self, title: str, tracks: list[Track], genre: Genre, year: int,
                 label: str):
        super().__init__(title, tracks, genre, year)
        self.__label = label

    @property
    def label(self):
        return self.__label

    @classmethod
    def from_album(cls, album: Album, label: str):
        return cls(album.title, album.tracks, album.genre, album.year, label)


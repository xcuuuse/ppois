from base.track import Track
from base.genre import Genre


class Album:
    def __init__(self, title: str, tracks: list[Track], genre: Genre, year: int):
        self._title = title
        self._tracks = tracks
        self._genre = genre
        self._year = year

    @property
    def title(self):
        return self._title

    @property
    def tracks(self):
        return [i.title for i in self._tracks]

    @property
    def genre(self):
        return self._genre.genre_name

    @property
    def year(self):
        return self._year




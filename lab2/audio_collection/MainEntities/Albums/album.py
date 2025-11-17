from MainEntities.track import Track
from MainEntities.genre import Genre
from MainEntities.label import Label
from Community.rating import Rating
from IdManage.album_id import AlbumId


class Album:
    """
    Album base class
    """
    def __init__(self, title: str, tracks: list[Track], genre: Genre, year: int,
                 label: Label):
        """
        Constructor
        :param title: Album title
        :param tracks: Album tracks
        :param genre: Album genre
        :param year: Album year
        :param label: Album label
        """
        self._title = title
        self._tracks = tracks
        self._genre = genre
        self._year = year
        self._label = label
        self._max_single_tracks = 3
        self._max_ep_tracks = 7
        self._rating: list[Rating] = []
        self._id = AlbumId.generate_id()
        self._likes = 0

    @property
    def title(self):
        return self._title

    @property
    def tracks(self):
        return self._tracks

    @property
    def genre(self):
        return self._genre.genre_name

    @property
    def year(self):
        return self._year

    @property
    def label(self):
        return self._label

    @property
    def rating(self):
        return self._rating

    @property
    def album_id(self):
        return self._id

    @property
    def likes(self):
        return self._likes

    def get_liked(self):
        self._likes += 1

    def get_info(self):
        return f"{self._title}. [{self._tracks}]"

    def average_rating(self):
        if not self._rating:
            return 0
        return sum(r for r in self._rating) / len(self._rating)

    def add_rating(self, rating: Rating):
        if 1 <= int(rating) <= 5:
            self._rating.append(rating)
        else:
            raise ValueError("Rating must be between 1 and 5")

    def total_duration(self):
        return sum(track.duration.duration for track in self._tracks)
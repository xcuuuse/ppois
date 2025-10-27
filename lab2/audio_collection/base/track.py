from base.genre import Genre
from id_manage.track_id import TrackId

class Track:
    def __init__(self, title: str, duration: int, genre: Genre):
        self.__title = title
        self.__duration = duration
        self.__genre = genre
        self.__track_id = TrackId.generate_id()

    @property
    def title(self):
        return self.__title

    @property
    def duration(self):
        return self.__duration

    @property
    def genre(self):
        return self.__genre

    @property
    def track_id(self):
        return self.__track_id

    def formated_duration(self):
        minutes = self.__duration // 60
        seconds = self.__duration - minutes * 60
        return f"{minutes}:{seconds}" if seconds >= 10 else f"{minutes}:0{seconds}"



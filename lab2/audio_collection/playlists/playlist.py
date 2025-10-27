from base.track import Track


class Playlist:
    def __init__(self, name: str, tracks: list[Track]):
        self.__name = name
        self.__tracks = tracks
        self.__duration = sum([i.duration for i in self.__tracks])

    @property
    def name(self):
        return self.__name

    @property
    def tracks(self):
        return self.__tracks

    @property
    def duration(self):
        return self.__duration

    def get_formated_duration(self):
        minutes = self.__duration // 60
        seconds = self.__duration - minutes * 60
        return f"{minutes}:{seconds}" if seconds >= 10 else f"{minutes}:0{seconds}"

    def add_track(self, track: Track):
        if track.track_id not in [i.track_id for i in self.__tracks]:
            self.__tracks.append(track)
        else:
            # raise an exception
            pass

    def playlist_tracks(self):
        return [i.title for i in self.__tracks]

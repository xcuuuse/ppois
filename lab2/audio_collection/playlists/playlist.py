from Base.track import Track
from Exceptions.track_adding_error import TrackAddingError
from Playback.queue import Queue


class Playlist:
    def __init__(self, name: str):
        self.__name = name
        self.__tracks = []
        self.__duration = sum([i.duration for i in self.__tracks])
        self.__current_track = Track
        self.__queue = Queue()

    @property
    def name(self):
        return self.__name

    @property
    def current_track(self):
        return self.__current_track

    @property
    def tracks(self):
        return [i.title for i in self.__tracks]

    @property
    def duration(self):
        return self.__duration

    @property
    def queue(self):
        return self.__queue.show_queue()

    def get_formated_duration(self):
        minutes = self.__duration // 60
        seconds = self.__duration - minutes * 60
        return f"{minutes}:{seconds}" if seconds >= 10 else f"{minutes}:0{seconds}"

    def add_track(self, track: Track):
        if track.track_id in [i.track_id for i in self.__tracks]:
            raise TrackAddingError("The track is already in playlist")
        self.__tracks.append(track)

    def playlist_tracks(self):
        return [i.title for i in self.__tracks]

    def add_to_queue(self, track: Track, after_current: bool = True):
        if track.track_id not in [i.track_id for i in self.__tracks]:
            raise TrackAddingError("Track must be in playlist before adding to queue")
        if after_current:
            self.__queue.add_to_queue(track, self.__current_track)
        else:
            self.__queue.add_to_queue(track, None)

    def next_track(self):
        next_track = self.__queue.queue_next()
        if next_track:
            self.__current_track = next_track
        return self.current_track.title


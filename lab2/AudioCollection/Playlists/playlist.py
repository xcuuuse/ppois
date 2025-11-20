from MainEntities.track import Track
from Exceptions.track_adding_error import TrackAddingError
from Playback.queue import Queue
from Playlists.history import History


class Playlist:
    """
    Playlist base class
    """
    def __init__(self, name: str):
        """
        Constructor
        :param name: Playlist name
        """
        self.__name = name
        self._tracks: list[Track] = []
        self._duration = sum([i.duration for i in self._tracks])
        self._current_track: Track | None = None
        self.__queue = Queue()
        self.__history = History()

    @property
    def name(self):
        return self.__name

    @property
    def current_track(self):
        return self._current_track

    @property
    def tracks(self):
        return self._tracks

    @property
    def duration(self):
        return self._duration

    @property
    def queue(self):
        return self.__queue.show_queue()

    @property
    def history(self):
        self.__history.append(self.current_track)
        return self.__history

    def get_formated_duration(self):
        """
        Returns playlist duration as minutes:seconds
        :return:
        """
        minutes = self._duration // 60
        seconds = self._duration % 60
        return f"{minutes}:{seconds:02d}"

    def add_track(self, track: Track):
        """
        Adds track to playlist
        :param track: Track to add
        :return: Updated playlist tracks
        """
        if (track.track_id in [i.track_id for i in self._tracks] or
                track.normalized_name in [i.normalized_name for i in self._tracks]):
            raise TrackAddingError("The track is already in playlist")

        self._tracks.append(track)
        self._duration += track.duration
        if self._current_track is None:
            self._current_track = track

    def delete_track(self, track: Track):
        """
        Deletes a track from playlist
        :param track: Track to delete
        :return: Updated playlist tracks
        """
        if track in self._tracks:
            self._tracks.remove(track)

    def playlist_tracks(self):
        """
        Returns all playlist tracks
        :return: playlist tracks
        """
        return [i.title for i in self._tracks]

    def next_track(self):
        """
        Goes to next track
        """
        next_track = self.__queue.queue_next()
        if next_track:
            self._current_track = next_track
        return self.current_track.title if self._current_track else None

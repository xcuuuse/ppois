from MainEntities.track import Track
from Playlists.favourite import Favourite
from Playlists.playlist import Playlist
from Exceptions.track_adding_error import TrackAddingError


class FavouriteTracks(Playlist, Favourite):
    """
    Favourite tracks class
    """
    def __init__(self):

        Playlist.__init__(self, name="Favourite Tracks")
        Favourite.__init__(self)

    def add_track(self, track: Track):
        """
        Adds track to favourite
        :param track: Track to like
        :return: Updated favourite tracks
        """
        if track in self._tracks:
            raise TrackAddingError("Track already in favourites")
        self._tracks.append(track)
        self._objects.append(track)
        self._duration += track.duration

        if self._current_track is None:
            self._current_track = track

    def delete_track(self, track: Track):
        """
        Deletes track from favourite
        :param track: Track to delete
        :return: Updated fav tracks
        """
        if track in self._objects:
            self._objects.remove(track)
        if track in self._tracks:
            self._tracks.remove(track)

    @property
    def tracks(self):
        return [i for i in self.objects if isinstance(i, Track)]

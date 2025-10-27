from playlists.playlist import Playlist
from base.track import Track, TrackId


class Collection:
    def __init__(self, playlist: Playlist):
        self.__playlist = playlist

    @property
    def playlist(self):
        return self.__playlist.name



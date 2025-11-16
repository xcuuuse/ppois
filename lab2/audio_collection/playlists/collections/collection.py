from Playlists.playlist import Playlist
from MainEntities.track import Track, TrackId


class Collection:
    """
    Collection base class
    """
    def __init__(self, playlist: Playlist):
        """
        Constructor
        :param playlist: A playlist to create collection from
        """
        self.__playlist = playlist

    @property
    def playlist(self):
        return self.__playlist.name



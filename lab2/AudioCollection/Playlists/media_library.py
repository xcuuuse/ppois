from Playlists.playlist import Playlist
from MainEntities.Artists.artist import Artist
from MainEntities.Albums.album import Album
from Exceptions.type_error import TypeError
from Playlists.favourite_tracks import FavouriteTracks


class MediaLibrary:
    """
    Media library class
    """
    def __init__(self):
        self.__playlists: list[Playlist] = []
        self.__artists: list[Artist] = []
        self.__albums: list[Album] = []
        self.__favourite_tracks = FavouriteTracks()

    @property
    def favourite_tracks(self):
        return self.__favourite_tracks.objects

    def add_favourite_track(self, track):
        """
        Adds track to fav
        """
        self.__favourite_tracks.add_track(track)

    @property
    def playlists(self):
        return self.__playlists

    @property
    def artists(self):
        return self.__artists

    @property
    def albums(self):
        return self.__albums

    def add_to_library(self, target: object):
        """
        Adds object to library
        :param target:Object to add to library
        :return: Updated library
        """
        from MainEntities.track import Track
        if not isinstance(target, (Playlist, Album, Artist, Track)):
            raise TypeError("Target must be a Playlist, Album or Artist or Track")
        if isinstance(target, Playlist):
            self.__playlists.append(target)
        elif isinstance(target, Album):
            self.__albums.append(target)
        else:
            self.__artists.append(target)

        if isinstance(target, Track):
            self.add_favourite_track(target)

    def pin_artist(self, artist: Artist):
        """
        Pins an artist
        :param artist: Artist to pin
        """
        if artist in self.__artists:
            self.__artists.remove(artist)
            self.__artists.insert(0, artist)

    def pin_album(self, album: Album):
        """
        Pins an album
        :param album: Album to pin
        """
        if album in self.__albums:
            self.__albums.remove(album)
            self.__albums.insert(0, album)

    def pin_playlist(self, playlist: Playlist):
        """
        Pins a playlist
        :param playlist: Playlist to pin
        """
        if playlist in self.__playlists:
            self.__playlists.remove(playlist)
            self.__playlists.insert(0, playlist)

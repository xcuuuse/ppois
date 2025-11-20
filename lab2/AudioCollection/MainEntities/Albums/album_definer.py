from MainEntities.Albums.single import Single
from MainEntities.Albums.studio_album import StudioAlbum
from MainEntities.Albums.ep import Ep
from MainEntities.Albums.album import Album


class AlbumDefiner:
    """
    Album definer class
    """
    @classmethod
    def define(cls, album: Album):
        """
        Defines album(single, ep, or full-format album)
        :param album: Album to define type
        :return: Album type
        """
        tracks_count = len(album.tracks)

        if tracks_count <= 3:
            return Single(album.title, album.tracks, album._genre, album.year, album.label)
        elif 4 <= tracks_count <= 6:
            return Ep(album.title, album.tracks, album._genre, album.year, album.label)
        else:
            return StudioAlbum(album.title, album.tracks, album._genre, album.year, album.label)


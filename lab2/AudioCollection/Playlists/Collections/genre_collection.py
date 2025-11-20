from Playlists.Collections.collection import Playlist, Collection
from MainEntities.genre import Genre


class GenreCollection(Collection):
    """
    Genre collection class
    """
    def __init__(self, playlist: Playlist, genre: Genre):
        """
        Constructor
        :param playlist: A playlist to create genre collection from
        :param genre: Collection genre
        """
        super().__init__(playlist)
        self.__tracks = playlist.tracks
        self.__genre = genre

    @property
    def genre(self):
        return self.__genre

    @property
    def tracks(self):
        """
        Returns collection tracks
        :return: collection tracks
        """
        new_tracks = []
        for i in self.__tracks:
            if i.genre.genre_name == self.__genre.genre_name:
                new_tracks.append(i)
        return new_tracks




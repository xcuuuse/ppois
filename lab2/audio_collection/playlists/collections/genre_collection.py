from playlists.collections.collection import Playlist, Collection
from base.genre import Genre


class GenreCollection(Collection):
    def __init__(self, playlist: Playlist, genre: Genre):
        super().__init__(playlist)
        self.__tracks = playlist.tracks
        self.__genre = genre

    @property
    def genre(self):
        return self.__genre

    @property
    def tracks(self):
        new_tracks = []
        for i in self.__tracks:
            if i.genre.genre_name == self.__genre.genre_name:
                new_tracks.append(i)
        return new_tracks

    def collection_tracks(self):
        return [i.title for i in self.tracks]




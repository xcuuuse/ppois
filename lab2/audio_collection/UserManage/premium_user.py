from UserManage.user import User, Username
from Playlists.Collections.genre_collection import Genre, GenreCollection
from Playlists.playlist import Playlist


class PremiumUser(User):
    def __init__(self, username: Username, months: int):
        super().__init__(username)
        self.__playlists = []
        self.__months = months
        self.__max_playlists = 20
        self.__collections = []

    @property
    def months(self):
        return self.__months

    @property
    def collections(self):
        return self.__collections

    def create_collection(self, playlist: Playlist, genre: Genre):
        if playlist in self.__playlists:
            self.__collections.append(GenreCollection(playlist, genre))
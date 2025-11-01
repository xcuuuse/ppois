from UserManage.username import Username
from Playlists.playlist import Playlist
from Exceptions.playlist_deleting_error import PlaylistDeleteError
from Subscription.personal_account import PersonalAccount


class User:
    def __init__(self, username: Username):
        self.__username = username
        self.__playlists = []
        self.__max_playlists = 10
        self.__amount = PersonalAccount(0)

    @property
    def username(self):
        return self.__username

    @property
    def playlists(self):
        return self.__playlists

    @property
    def amount(self):
        return self.__amount.amount

    def create_playlist(self, playlist_name: str):
        while len(self.__playlists) <= self.__max_playlists:
            self.__playlists.append(Playlist(playlist_name))

    def delete_playlist(self, name_to_delete):
        if name_to_delete not in [i.name for i in self.__playlists]:
            raise PlaylistDeleteError("You have no playlists with such name, try again")
        self.__playlists.remove(Playlist(name_to_delete))

    def add_to_amount(self, add_value: int):
        self.__amount.add_to_amount(add_value)

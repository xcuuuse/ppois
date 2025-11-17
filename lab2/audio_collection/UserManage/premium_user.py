from UserManage.user import User, Username
from Playlists.Collections.genre_collection import Genre, GenreCollection
from Playlists.playlist import Playlist
from UserManage.user_profile import UserProfile
from Subscription.subscription import Subscription
from Playlists.Collections.collection import Collection

class PremiumUser(User):
    """
    Premium user class
    """
    def __init__(self, username: Username, profile: UserProfile, subscription: Subscription):
        """
        Constructor
        :param username: Premium user username
        :param profile: Premium user profile
        :param subscription: Subscription
        """
        super().__init__(username, profile)
        self.__playlists = []
        self.__subscription = subscription
        self.__max_playlists = 20
        self.__collections: list[Collection] = []

    @property
    def months(self):
        return self.__subscription.months

    @property
    def collections(self):
        return self.__collections

    def create_collection(self, playlist: Playlist, genre: Genre):
        """
        Creates collection from a selected playlists
        :param playlist: Playlist to create a collection from
        :param genre: Genre to create a collection on
        """
        if playlist in self.__playlists:
            self.__collections.append(GenreCollection(playlist, genre))

    def extend_subscription(self, months):
        self.__subscription.extend_subscription(months)
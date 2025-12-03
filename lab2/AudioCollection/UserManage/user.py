from Community.comment import Comment
from Community.rating import Rating
from Community.like import Like
from Exceptions.playlist_deleting_error import PlaylistDeleteError
from Exceptions.resources_error import ResourcesError
from IdManage.user_id import UserId
from MainEntities.Artists.concert import Concert
from MainEntities.Artists.ticket import Ticket
from UserManage.username import Username
from Playlists.media_library import MediaLibrary
from Playlists.playlist import Playlist
from Subscription.personal_account import PersonalAccount
from Subscription.subscription import Subscription
from UserManage.user_profile import UserProfile
from Playlists.favourite_tracks import FavouriteTracks


class User:
    """
    User base class
    """
    def __init__(self, username: Username, profile: UserProfile):
        """
        Constructor
        :param username: User username
        :param profile: User proile
        """
        self.__username = username
        self.__media: MediaLibrary = MediaLibrary()
        self.__max_playlists = 10
        self.__amount = PersonalAccount(0)
        self.__subscription = Subscription(0)
        self.__comments: list[Comment] = []
        self.__profile = profile
        self._user_id = UserId.generate_id()
        self.__likes: list[Like] = []
        self.__tickets: list[Ticket] = []
        self.__favourite_tracks = FavouriteTracks()


    @property
    def username(self):
        return self.__username.username

    @property
    def playlists(self):
        return self.__media.playlists

    @property
    def amount(self):
        return self.__amount.amount

    @property
    def profile(self):
        return self.__profile

    @property
    def likes(self):
        return self.__likes

    @property
    def favourite_tracks(self):
        return self.__favourite_tracks.tracks

    @property
    def media(self):
        return self.__media

    def like(self, target: object):
        """
        Likes an object
        :param target: Object to like
        """
        from MainEntities.track import Track
        from MainEntities.Albums.album import Album
        from MainEntities.Artists.artist import Artist

        if not isinstance(target, (Track, Album, Artist)):
            raise TypeError("You can only like Track, Album or Artist")

        like = Like(target)
        self.__likes.append(like)
        if isinstance(target, Track):
            self.__favourite_tracks.add_track(target)

        self.__media.add_to_library(target)

    def create_playlist(self, playlist_name: str):
        """
        Creates a user playlist
        :param playlist_name: Playlist name
        :return: Updated user media
        """
        if len(self.__media.playlists) >= self.__max_playlists:
            raise PlaylistDeleteError("Maximum number of playlists reached.")
        self.__media.add_to_library(Playlist(playlist_name))

    def delete_playlist(self, name_to_delete: str):
        """
        Deletes selected playlist
        :param name_to_delete: Playlist to delete
        :return: Updated media library
        """
        playlist_to_delete = None
        for playlist in self.__media.playlists:
            if playlist.name == name_to_delete:
                playlist_to_delete = playlist
                break

        if playlist_to_delete is None:
            raise PlaylistDeleteError("You have no playlists with such name, try again")

        self.__media.playlists.remove(playlist_to_delete)

    def add_to_amount(self, add_value: int):
        """
        Adds value to user amount
        :param add_value: Value to add
        """
        self.__amount.add_to_amount(add_value)

    def comment_track(self, track, text: str):
        """
        Comments a track
        :param track: Track to comment
        :param text: A comment
        """
        track.add_comment(self, text)
        self.__comments.append(Comment(text))

    @staticmethod
    def rate_track(track, rate: int):
        """
        Rates the track
        :param track: Track to rate
        :param rate: Personal rating
        """
        from Exceptions.rating_error import RatingError
        if not 1 <= rate <= 5:
            raise RatingError("Rating must be from 1 to 5")
        track.add_rate(Rating(rate))

    def update_bio(self, new_bio: str):
        """
        Updates user bio
        :param new_bio: new bio
        :return: Updated bio
        """
        self.__profile.bio = new_bio

    def buy_ticket(self, concert: Concert):
        """
        Buys a ticket to a concert
        :param concert: concert
        """
        if self.__amount <= concert.ticket_price:
            raise ResourcesError("You have lack of resources to continue the operation")
        concert.sell_ticket()
        self.__tickets.append(Ticket(concert))
        self.__amount -= concert.ticket_price

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from MainEntities.Albums.album import Album


class Artist:
    """
    Artist base class
    """
    def __init__(self, name: str, albums: list["Album"]):
        """
        Constructor
        :param name: Artist name
        :param albums: Artist albums
        """
        self._name = name
        self._albums = albums
        self._followers: int = 0

    @property
    def name(self):
        return self._name

    @property
    def albums(self):
        return self._albums

    @property
    def followers(self):
        return self._followers

    def get_album_info(self, album):
        """
        A method to get the album info
        :param album:
        :return:
        """
        if album in self._albums:
            return f"{album.title} - {self._name}. {album.year}, {album.genre}"

    def get_followed(self):
        self._followers += 1


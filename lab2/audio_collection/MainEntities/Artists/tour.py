from MainEntities.Artists.artist import Artist
from MainEntities.Artists.concert import Concert


class Tour:
    """
    Tour class
    """
    def __init__(self, artist: Artist, concerts: list[Concert]):
        """
        Constructor
        :param artist: Artist
        :param concerts: Tour concerts
        """
        self.__artist = artist
        self.__concerts = concerts
        self.__ticket_amount = sum(i.ticket_amount for i in self.__concerts)
        self.__cities = [i.city for i in concerts]

    @property
    def artist(self):
        return self.__artist

    @property
    def ticket_amount(self):
        return self.__ticket_amount

    @property
    def concerts(self):
        return self.__concerts

    @property
    def cities(self):
        return self.__cities

from MainEntities.Artists.artist import Artist
from MainEntities.date import Date
from MainEntities.city import City
from Exceptions.ticket_selling_error import TicketSellingError


class Concert:
    """
    Concert class
    """
    def __init__(self, artist: Artist, ticket_amount: int, city: City, date: Date):
        """
        Constructor
        :param artist: Artist
        :param ticket_amount: Amount of tickets
        :param city: Concert city
        :param date: Concert date
        """
        self.__artist = artist
        self.__ticket_amount = ticket_amount
        self.__city = city
        self.__date = date
        self.__ticket_price: int = 0

    @property
    def artist(self):
        return self.__artist

    @property
    def ticket_amount(self):
        return self.__ticket_amount

    @property
    def city(self):
        return self.__city

    @property
    def date(self):
        return self.__date

    @property
    def ticket_price(self):
        return self.__ticket_price

    def sell_ticket(self):
        if self.__ticket_amount == 0:
            raise TicketSellingError("Sold out")
        self.__ticket_amount -= 1

    

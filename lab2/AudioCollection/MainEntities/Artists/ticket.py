from MainEntities.Artists.concert import Concert
from IdManage.ticket_id import TicketId


class Ticket:
    """
    Ticket class
    """
    def __init__(self, concert: Concert):
        """
        Constructor
        :param concert: Concert
        """
        self.__concert = concert
        self.__ticket_id = TicketId.generate_id()
        self.__is_used = False
        self.__seat_number = None
        self.__price = concert.ticket_price

    @property
    def concert(self):
        return self.__concert

    @property
    def ticket_id(self):
        return self.__ticket_id

    @property
    def is_used(self):
        return self.__is_used

    @property
    def seat_number(self):
        return self.__seat_number

    @property
    def price(self):
        return self.__price

    def use_ticket(self):
        """
        Marks the ticket as used.
        :return: True if ticket was successfully used, False if already used
        """
        if self.__is_used:
            return False
        self.__is_used = True
        return True

    def assign_seat(self, seat_number: str):
        """
        Assign a seat number to the ticket
        :param seat_number: Seat identifier
        """
        self.__seat_number = seat_number

    def get_ticket_info(self):
        """
        Returns detailed ticket information
        :return: dict with ticket ID, concert, seat, price, and used status
        """
        return {
            "ticket_id": self.__ticket_id,
            "artist": self.__concert.artist,
            "seat_number": self.__seat_number,
            "price": self.__price,
            "is_used": self.__is_used
        }
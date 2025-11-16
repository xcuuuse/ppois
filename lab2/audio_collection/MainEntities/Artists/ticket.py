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

    @property
    def concert(self):
        return self.__concert

    @property
    def ticket_id(self):
        return self.__ticket_id

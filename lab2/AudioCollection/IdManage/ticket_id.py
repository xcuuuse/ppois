from IdManage.id_generator import IdGenerator


class TicketId(IdGenerator):
    """
    Ticket id class
    """
    __ticket_id = 0

    @classmethod
    def generate_id(cls):
        """
        Generates ticket id
        :return: ticket id
        """
        cls.__ticket_id += 1
        return cls.__ticket_id

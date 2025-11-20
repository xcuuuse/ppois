class PersonalAccount:
    """
    Personal account class
    """
    def __init__(self, amount: int):
        """
        Constructor
        :param amount: Amount on account
        """
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    def add_to_amount(self, amount_to_add: int):
        """
        Adds amount to account
        :param amount_to_add: Amount to add to account
        :return: Updated amount
        """
        self.__amount += amount_to_add

    def subtract_from_amount(self, amount_to_subtract: int):
        """
        Subtracts amount from account
        :param amount_to_subtract: Amount to subtract from account
        :return: Updated amount
        """
        self.__amount -= amount_to_subtract


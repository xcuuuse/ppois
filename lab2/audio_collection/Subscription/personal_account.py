class PersonalAccount:
    def __init__(self, amount: int):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    def add_to_amount(self, amount_to_add: int):
        self.__amount += amount_to_add

    def subtract_from_amount(self, amount_to_subtract: int):
        self.__amount -= amount_to_subtract


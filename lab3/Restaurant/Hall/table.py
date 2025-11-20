from dataclasses import dataclass


@dataclass
class Table:
    __number: int
    __seats: int
    __is_reserved: bool = False

    @property
    def number(self):
        return self.__number

    @property
    def seats(self):
        return self.__seats

    @property
    def is_reserved(self):
        return self.__is_reserved

    def reserve(self, amount):
        from Exceptions.table_reserving_error import TableReservingError
        if amount > self.__seats:
            raise TableReservingError(f"The amount of people has to be less than {self.__seats + 1}")
        if self.__is_reserved:
            raise TableReservingError(f"The table is already reserved")
        self.__is_reserved = True
        self.__seats -= amount

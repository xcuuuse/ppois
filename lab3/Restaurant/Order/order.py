from Order.order_item import OrderItem
from Hall.table import Table


class Order:
    def __init__(self, table: Table, items: list[OrderItem]):
        self.__table = table
        self.__items = items



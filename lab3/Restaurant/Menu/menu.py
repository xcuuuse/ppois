from Menu.menu_item import MenuItem
from Exceptions.item_error import ItemError


class Menu:
    def __init__(self):
        self.__items: dict[int, MenuItem] = {}

    @property
    def items(self):
        return self.__items

    def add_item(self, new_item: MenuItem):
        if new_item.item_id in self.__items:
            raise ItemError("Item is already in menu")
        self.__items[new_item.item_id] = new_item

    def get_item(self, item_id: int):
        return self.__items.get(item_id)

    def remove_item(self, item_id: int):
        if item_id in self.__items.keys():
            del self.__items[item_id]

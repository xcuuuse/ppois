from dataclasses import dataclass
from Menu.menu_item import MenuItem

@dataclass
class OrderItem:
    menu_item: MenuItem.item_id
    quantity: int


from dataclasses import dataclass


@dataclass
class MenuItem:
    _item_id: int
    _name: str
    _price: float
    _is_available: bool

    @property
    def item_id(self):
        return self._item_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def is_available(self):
        return self._is_available


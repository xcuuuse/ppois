from dataclasses import dataclass, field


@dataclass
class Employee:
    _name: str
    _position: str

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

from dataclasses import dataclass, field


@dataclass
class Employee:
    _name: str
    _salary: float
    _employee_id: int

    @property
    def name(self):
        return self._name

    @property
    def employee_id(self):
        return self._employee_id

    def increase_salary(self, new_amount: float):
        self._salary += new_amount


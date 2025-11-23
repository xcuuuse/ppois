from Employee.employee import Employee


class EmployeeManager:
    def __init__(self):
        self.__employees: dict[int, Employee] = {}

    @property
    def employees(self):
        return self.__employees

    def add_employee(self, new_employee: Employee):
        self.__employees[new_employee.employee_id] = new_employee

    def adjust_employee_salary(self, employee_id: int, amount: float):
        employee = self.__employees.get(employee_id)
        employee.increase_salary(amount)

    def fine_employee(self, employee_id: int, amount: float):
        employee = self.__employees.get(employee_id)
        employee.increase_salary(-amount)

    def fire_employee(self, employee_id: int):
        del self.__employees[employee_id]

    
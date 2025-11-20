from Employee.employee import Employee


class EmployeeManager:
    def __init__(self):
        self.__employees: dict[int, Employee] = {}

    def add_employee(self, new_employee: Employee):
        self.__employees[new_employee.employee_id] = new_employee

    def adjust_salary(self, employee_id: int, amount: float):
        employee = self.__employees.get(employee_id)
        employee.increase_salary(amount)

    def fine_employee(self, employee_id: int, amount: float):
        employee = self.__employees.get(employee_id)
        employee.increase_salary(-amount)


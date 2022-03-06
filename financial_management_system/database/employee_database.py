import operator
import threading
import typing

from financial_management_system.data_types import Employee


class EmployeeDatabase:
    """Class to keep track of the state of employees."""

    def __init__(self):
        self._employees = {}
        self._lock = threading.RLock()

    def add_employee(self, employee: Employee) -> bool:
        """Add a new employee to the database.

        Perform the following validations:
          - Unique SSN
          - No existing matching employee id

        Returns true if a unique employee was added, or false if already present.
        A ValueError is raised if the SSN is not unique!
        """

        with self._lock:
            if employee.employee_id in self._employees:
                return False

            for tracked_employee in self._employees.values():
                if tracked_employee.ssn == employee.ssn:
                    raise ValueError(
                        f"Cannot add employee with ssn {employee.ssn}-- already exists: {tracked_employee}!"
                    )

            self._employees[employee.employee_id] = employee
            return True

    def has_employee(self, employee_id: str) -> bool:
        """Return true if the employee with the given ID is tracked in the database."""
        with self._lock:
            return employee_id in self._employees

    def get_employee(self, employee_id: str) -> typing.Optional[Employee]:
        """Return the tracked employee with the given ID, or None if there exists no such employee."""
        with self._lock:
            return self._employees.get(employee_id)

    def remove_employee(self, employee_id: str) -> bool:
        """Attempt to remove an employee from the database with the given ID.
        If no such employee can be removed, return False.
        """
        with self._lock:
            if employee_id in self._employees:
                del self._employees[employee_id]
                return True

            return False

    @property
    def employees(self) -> typing.List[Employee]:
        """Return a list of tracked employees, sorted alphabetically by last name."""

        with self._lock:
            return [
                *sorted(
                    self._employees.values(),
                    key=operator.attrgetter("first_name", "last_name"),
                )
            ]

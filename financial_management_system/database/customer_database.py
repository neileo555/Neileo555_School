import contextlib
import operator
import threading
import typing

from financial_management_system.data_types import Customer


class CustomerDatabase:
    """Class to keep track of the state of customers."""

    def __init__(self):
        self._customers = {}
        self._lock = threading.RLock()

    def add_customer(self, customer: Customer) -> bool:
        """Add a customer to the database, if it has not already been added."""

        with self._lock:
            if customer.customer_id in self._customers:
                return False
            else:
                self._customers[customer.customer_id] = customer
                return True

    def has_customer(self, customer_id: str) -> bool:
        """Return true if the given customer exists"""

        with self._lock:
            return customer_id in self._customers

    def get_customer(self, customer_id: str) -> typing.Optional[Customer]:
        """If there is a customer with the given Id, return the customer object.

        Otherwise, return None.
        """

        with self._lock:
            return self._customers.get(customer_id)

    def remove_customer(self, customer_id: str) -> bool:
        """Attempt to remove a customer from the database, and return true if a customer was removed."""

        with self._lock:
            if customer_id in self._customers:
                del self._customers[customer_id]
                return True

            return False

    @property
    def customers(self) -> typing.List[Customer]:
        """Return a list of tracked customers, sorted alphabetically by name."""

        with self._lock:
            return [*sorted(self._customers.values(), key=operator.attrgetter("name"))]

    @contextlib.contextmanager
    def lock(self):
        with self._lock:
            yield

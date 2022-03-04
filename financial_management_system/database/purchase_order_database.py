from financial_management_system.data_types import PurchaseOrder
import threading
import typing
import operator


class PurchaseOrderDatabase:
    """Class to keep track of the state of purchase_orders."""

    def __init__(self):
        self._purchase_orders = {}
        self._lock = threading.RLock()

    def add_purchase_order(self, purchase_order: PurchaseOrder) -> bool:
        """Add a new purchase order to the database.

        Perform the following validations:
          - No existing matching purchase order id

        Returns true if a unique purchase order was added, or false if already present.
        """

        with self.lock:
            if purchase_order.purchase_order_id in self._purchase_orders:
                return False
            else:
                self._purchase_orders[purchase_order.purchase_order_id] = purchase_order
                return True

    def has_purchase_order(self, purchase_order_id: str) -> bool:
        """Return true if the purchase order with the given ID is tracked in the database."""
        with self._lock:
            return purchase_order_id in self._purchase_orders

    def get_purchase_order(self, purchase_order_id: str) -> typing.Optional[PurchaseOrder]:
        """Return the tracked purchase order with the given ID, or None if there exists no such purchase_order."""
        with self._lock:
            return self._purchase_orders.get(purchase_order_id)

    def remove_purchase_order(self, purchase_order_id: str) -> bool:
        """Attempt to remove an purchase order from the database with the given ID.
        If no such purchase order can be removed, return False.
        """
        with self._lock:
            if purchase_order_id in self._purchase_orders:
                del self._purchase_orders[purchase_order_id]
                return True

            return False

    @property
    def purchase_orders(self) -> typing.List[PurchaseOrder]:
        """Return a list of tracked purchase orders, sorted alphabetically by last name."""

        with self._lock:
            return [*sorted(self._purchase_orders.values(), key=operator.attrgetter("date"))]

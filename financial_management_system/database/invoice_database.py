import operator
import threading
import typing

from financial_management_system.data_types import Invoice


class InvoiceDatabase:
    """Class to keep track of the state of invoices."""

    def __init__(self):
        self._invoices = {}
        self._lock = threading.RLock()

    def add_invoice(self, invoice: Invoice) -> bool:
        """Add a new invoice to the database.

        Perform the following validations:
          - No existing matching invoice id

        Returns true if a unique invoice was added, or false if already present.
        """

        with self.lock:
            if invoice.invoice_id in self._invoices:
                return False
            else:
                self._invoices[invoice.invoice_id] = invoice
                return True

    def has_invoice(self, invoice_id: str) -> bool:
        """Return true if the invoice with the given ID is tracked in the database."""
        with self._lock:
            return invoice_id in self._invoices

    def get_invoice(self, invoice_id: str) -> typing.Optional[Invoice]:
        """Return the tracked invoice with the given ID, or None if there exists no such invoice."""
        with self._lock:
            return self._invoices.get(invoice_id)

    def remove_invoice(self, invoice_id: str) -> bool:
        """Attempt to remove an invoice from the database with the given ID.
        If no such invoice can be removed, return False.
        """
        with self._lock:
            if invoice_id in self._invoices:
                del self._invoices[invoice_id]
                return True

            return False

    @property
    def invoices(self) -> typing.List[Invoice]:
        """Return a list of tracked invoices, sorted alphabetically by last name."""

        with self._lock:
            return [*sorted(self._invoices.values(), key=operator.attrgetter("date"))]

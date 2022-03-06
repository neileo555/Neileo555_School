import contextlib
import operator
import threading
import typing

from financial_management_system.data_types import Vendor


class VendorDatabase:
    """Class to keep track of the state of vendors."""

    def __init__(self):
        self._vendors = {}
        self._lock = threading.RLock()

    def add_vendor(self, vendor: Vendor) -> bool:
        """Add a vendor to the database, if it has not already been added."""

        with self._lock:
            if vendor.vendor_id in self._vendors:
                return False
            else:
                self._vendors[vendor.vendor_id] = vendor
                return True

    def has_vendor(self, vendor_id: str) -> bool:
        """Return true if the given vendor exists"""

        with self._lock:
            return vendor_id in self._vendors

    def get_vendor(self, vendor_id: str) -> typing.Optional[Vendor]:
        """If there is a vendor with the given Id, return the vendor object.

        Otherwise, return None.
        """

        with self._lock:
            return self._vendors.get(vendor_id)

    def remove_vendor(self, vendor_id: str) -> bool:
        """Attempt to remove a vendor from the database, and return true if a vendor was removed."""

        with self._lock:
            if vendor_id in self._vendors:
                del self._vendors[vendor_id]
                return True

            return False

    @property
    def vendors(self) -> typing.List[Vendor]:
        """Return a list of tracked vendors, sorted alphabetically by name."""

        with self._lock:
            return [*sorted(self._vendors.values(), key=operator.attrgetter("name"))]

    @contextlib.contextmanager
    def lock(self):
        with self._lock:
            yield

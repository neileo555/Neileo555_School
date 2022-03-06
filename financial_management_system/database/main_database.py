"""
"""

import contextlib
import typing

from financial_management_system.data_types import (
    Customer,
    Employee,
    Invoice,
    PurchaseOrder,
    Vendor,
)
from financial_management_system.database.customer_database import CustomerDatabase
from financial_management_system.database.employee_database import EmployeeDatabase
from financial_management_system.database.invoice_database import InvoiceDatabase
from financial_management_system.database.purchase_order_database import (
    PurchaseOrderDatabase,
)
from financial_management_system.database.vendor_database import VendorDatabase


class MainDatabase:
    """Central Database for keeping track of all databases used by the Financial Management System."""

    def __init__(self):

        self._customer_database = CustomerDatabase()
        self._employee_database = EmployeeDatabase()
        self._invoice_database = InvoiceDatabase()
        self._purchase_order_database = PurchaseOrderDatabase()
        self._vendor_database = VendorDatabase()

    ####################
    # Customer Methods #
    ####################

    def add_customer(self, customer: Customer) -> bool:
        """Add a customer to the database, if it has not already been added."""

        return self._customer_database.add_customer(customer)

    def has_customer(self, customer_id: str) -> bool:
        """Return true if the given customer exists"""

        return self._customer_database.has_customer(customer_id)

    def get_customer(self, customer_id: str) -> typing.Optional[Customer]:
        """If there is a customer with the given Id, return the customer object.

        Otherwise, return None.
        """

        return self._customer_database.get_customer(customer_id)

    def remove_customer(self, customer_id: str) -> bool:
        """Attempt to remove a customer from the database, and return true if a customer was removed."""

        return self._customer_database.remove_customer(customer_id)

    @property
    def customers(self) -> typing.List[Customer]:
        """Return a list of tracked customers, sorted alphabetically by name."""

        return self._customer_database.customers

    @contextlib.contextmanager
    def customer_lock(self):
        with self._customer_database.lock():
            yield

    ####################
    # Employee Methods #
    ####################

    def add_employee(self, employee: Employee) -> bool:
        """Add a new employee to the database.

        Perform the following validations:
          - Unique SSN
          - No existing matching employee id

        Returns true if a unique employee was added, or false if already present.
        A ValueError is raised if the SSN is not unique!
        """

        return self._employee_database.add_employee(employee)

    def has_employee(self, employee_id: str) -> bool:
        """Return true if the employee with the given ID is tracked in the database."""

        return self._employee_database.has_employee(employee_id)

    def get_employee(self, employee_id: str) -> typing.Optional[Employee]:
        """Return the tracked employee with the given ID, or None if there exists no such employee."""

        return self._employee_database.get_employee(employee_id)

    def remove_employee(self, employee_id: str) -> bool:
        """Attempt to remove an employee from the database with the given ID.
        If no such employee can be removed, return False.
        """

        return self._employee_database.remove_employee(employee_id)

    @property
    def employees(self) -> typing.List[Employee]:
        """Return a list of tracked employees, sorted alphabetically by last name."""

        return self._employee_database.employees

    @contextlib.contextmanager
    def employee_lock(self):
        with self._employee_database.lock():
            yield

    ###################
    # Invoice Methods #
    ###################

    def add_invoice(self, invoice: Invoice) -> bool:
        """Add a new invoice to the database.

        Perform the following validations:
          - No existing matching invoice id

        Returns true if a unique invoice was added, or false if already present.
        """

        return self._invoice_database.add_invoice(invoice)

    def has_invoice(self, invoice_id: str) -> bool:
        """Return true if the invoice with the given ID is tracked in the database."""

        return self._invoice_database.has_invoice(invoice_id)

    def get_invoice(self, invoice_id: str) -> typing.Optional[Invoice]:
        """Return the tracked invoice with the given ID, or None if there exists no such invoice."""

        return self._invoice_database.get_invoice(invoice_id)

    def remove_invoice(self, invoice_id: str) -> bool:
        """Attempt to remove an invoice from the database with the given ID.
        If no such invoice can be removed, return False.
        """

        return self._invoice_database.remove_invoice(invoice_id)

    @property
    def invoices(self) -> typing.List[Invoice]:
        """Return a list of tracked invoices, sorted alphabetically by last name."""

        return self._invoice_database.invoices

    @contextlib.contextmanager
    def invoice_lock(self):
        with self._invoice_database.lock():
            yield

    ##########################
    # Purchase Order Methods #
    ##########################

    def add_purchase_order(self, purchase_order: PurchaseOrder) -> bool:
        """Add a new purchase order to the database.

        Perform the following validations:
          - No existing matching purchase order id

        Returns true if a unique purchase order was added, or false if already present.
        """
        return self._purchase_order_database.add_purchase_order(purchase_order)

    def has_purchase_order(self, purchase_order_id: str) -> bool:
        """Return true if the purchase order with the given ID is tracked in the database."""
        return self._purchase_order_database.has_purchase_order(purchase_order_id)

    def get_purchase_order(self, purchase_order_id: str) -> typing.Optional[PurchaseOrder]:
        """Return the tracked purchase order with the given ID, or None if there exists no such purchase_order."""
        return self._purchase_order_database.get_purchase_order(purchase_order_id)

    def remove_purchase_order(self, purchase_order_id: str) -> bool:
        """Attempt to remove an purchase order from the database with the given ID.
        If no such purchase order can be removed, return False.
        """
        return self._purchase_order_database.remove_purchase_order(purchase_order_id)

    @property
    def purchase_orders(self) -> typing.List[PurchaseOrder]:
        """Return a list of tracked purchase orders, sorted alphabetically by last name."""
        return self._purchase_order_database.purchase_orders

    @contextlib.contextmanager
    def purchase_order_lock(self):
        with self._purchase_order_database.lock():
            yield

    ##################
    # Vendor Methods #
    ##################

    def add_vendor(self, vendor: Vendor) -> bool:
        """Add a vendor to the database, if it has not already been added."""
        return self._vendor_database.add_vendor(vendor)

    def has_vendor(self, vendor_id: str) -> bool:
        """Return true if the given vendor exists"""
        return self._vendor_database.has_vendor(vendor_id)

    def get_vendor(self, vendor_id: str) -> typing.Optional[Vendor]:
        """If there is a vendor with the given Id, return the vendor object.

        Otherwise, return None.
        """
        return self._vendor_database.get_vendor(vendor_id)

    def remove_vendor(self, vendor_id: str) -> bool:
        """Attempt to remove a vendor from the database, and return true if a vendor was removed."""
        return self._vendor_database.remove_vendor(vendor_id)

    @property
    def vendors(self) -> typing.List[Vendor]:
        """Return a list of tracked vendors, sorted alphabetically by name."""
        return self._vendor_database.vendors

    @contextlib.contextmanager
    def vendor_lock(self):
        with self._vendor_database.lock():
            yield

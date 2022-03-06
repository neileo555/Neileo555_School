import pathlib
from importlib import resources

from PyQt5 import QtWidgets, uic, QtCore
from financial_management_system.database import MainDatabase
from financial_management_system.windows import (
    customer_management_window,
    employee_management_window,
    financial_management_window,
    inventory_management_window,
    vendor_management_window,
)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        """ """

        super().__init__(parent)

        # Set up base database
        self.database = MainDatabase()

        # Render from Template
        uic.loadUi(self.template_path, self)

        # Close child popups when this closes
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # Set up Buttons
        self.customer_management_button.clicked.connect(self.handle_customer_management_click)
        self.employee_management_button.clicked.connect(self.handle_employee_management_click)
        self.vendor_management_button.clicked.connect(self.handle_vendor_management_click)
        self.financial_management_button.clicked.connect(self.handle_financial_management_click)
        self.inventory_management_button.clicked.connect(self.handle_inventory_management_click)

        # Set up child pages
        self.customer_management_window = None
        self.employee_management_window = None
        self.vendor_management_window = None
        self.financial_management_window = None
        self.inventory_management_window = None

    @property
    def template_path(self) -> pathlib.Path:
        """ """

        with resources.path("financial_management_system.templates", "main_window.ui") as template:
            return template

    #########################
    # Handle Button Presses #
    #########################

    def handle_customer_management_click(self) -> None:
        """ """

        self.customer_management_window = customer_management_window.CustomerManagementWindow(
            database=self.database, parent=self
        )
        self.customer_management_window.show()

    def handle_employee_management_click(self) -> None:
        """ """
        self.employee_management_window = employee_management_window.EmployeeManagementWindow(
            database=self.database, parent=self
        )
        self.employee_management_window.show()

    def handle_vendor_management_click(self) -> None:
        """ """
        self.vendor_management_window = vendor_management_window.VendorManagementWindow(
            database=self.database, parent=self
        )
        self.vendor_management_window.show()

    def handle_financial_management_click(self) -> None:
        """ """
        self.financial_management_window = financial_management_window.FinancialManagementWindow(
            database=self.database, parent=self
        )
        self.financial_management_window.show()

    def handle_inventory_management_click(self) -> None:
        """ """
        self.inventory_management_window = inventory_management_window.InventoryManagementWindow(
            database=self.database, parent=self
        )
        self.inventory_management_window.show()

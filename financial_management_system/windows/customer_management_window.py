import pathlib
import typing
from importlib import resources

from financial_management_system.database import MainDatabase
from PyQt5 import QtWidgets, uic


class CustomerManagementWindow(QtWidgets.QWidget):
    """ """

    def __init__(self, database: MainDatabase, parent: typing.Optional[QtWidgets.QWidget] = None):
        """ """
        super().__init__(parent)

        # Store Database Reference
        self.database = database

        # Rendor from Template
        uic.loadUi(self.template_path, self)

    @property
    def template_path(self) -> pathlib.Path:
        """ """

        with resources.path(
            "financial_management_system.templates", "employee_management.ui"
        ) as template:
            return template

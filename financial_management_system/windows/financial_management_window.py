import pathlib
from importlib import resources
import typing

from financial_management_system.database import MainDatabase
from financial_management_system.windows import base_window
from PyQt5 import QtWidgets, uic, QtCore


class FinancialManagementWindow(base_window.BaseWindow):
    """ """

    def __init__(self, database: MainDatabase, parent: typing.Optional[QtWidgets.QWidget] = None):
        """ """
        super().__init__(database, parent)

    @property
    def template_path(self) -> pathlib.Path:
        """ """

        with resources.path(
            "financial_management_system.templates", "employee_management.ui"
        ) as template:
            return template

import pathlib
from importlib import resources
import typing

from financial_management_system.database import MainDatabase
from PyQt5 import QtWidgets, uic, QtCore


class FinancialManagementWindow(QtWidgets.QWidget):
    """ """

    def __init__(self, database: MainDatabase, parent: typing.Optional[QtWidgets.QWidget] = None):
        """ """
        super().__init__(parent)

        # Store Database Reference
        self.database = database

        # Render from Template
        uic.loadUi(self.template_path, self)

        # Close child popups when this closes
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # Set margins to be nonexistent
        self.setContentsMargins(0, 0, 0, 0)

        # Tell QT that this window should be a popup window with its own "x button" that should be movable
        self.setWindowFlags(QtCore.Qt.Dialog)

        # Move the dialog to the widget that called it
        point = self.parent().rect().topRight()
        global_point = self.parent().mapToGlobal(point)
        self.move(global_point - QtCore.QPoint(self.width(), 0))

    @property
    def template_path(self) -> pathlib.Path:
        """ """

        with resources.path(
            "financial_management_system.templates", "employee_management.ui"
        ) as template:
            return template

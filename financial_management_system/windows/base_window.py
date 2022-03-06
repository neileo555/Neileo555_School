"""
"""

import abc
import pathlib
import typing

from financial_management_system.database import MainDatabase
from PyQt5 import QtCore, QtWidgets, uic


class BaseWindow(QtWidgets.QWidget):
    def __init__(self, database: MainDatabase, parent: typing.Optional[QtWidgets.QWidget] = None):

        super().__init__(parent)

        # Database to use for persistence
        self._database = database

        # Close child popups when this closes
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # Set margins to be nonexistent
        self.setContentsMargins(0, 0, 0, 0)

        # Tell QT that this window should be a popup window with its own "x button" that should be movable
        self.setWindowFlags(QtCore.Qt.Dialog)

        # Move the dialog to the widget that spawned it
        if parent is not None:
            point = self.parent().rect().topRight()
            global_point = self.parent().mapToGlobal(point)
            self.move(global_point - QtCore.QPoint(self.width(), 0))

        # Render Template Skeleton
        uic.loadUi(self.template_path, self)

    @property
    def template_path(self) -> pathlib.Path:
        """Path to the .ui template file for this widget"""

        raise NotImplementedError("One must define this property to use BaseWindow!")

    @property
    def database(self) -> MainDatabase:
        return self._database

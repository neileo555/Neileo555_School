from email.mime import base
from os import stat
import pathlib
import typing
from importlib import resources

from financial_management_system.data_types import Employee
from financial_management_system.database import MainDatabase
from financial_management_system.windows import base_window
from PyQt5 import QtWidgets, uic, QtCore


class AddEmployeeWindow(base_window.BaseWindow):
    """ """

    def __init__(
        self, database: MainDatabase, parent: typing.Optional[QtWidgets.QWidget] = None
    ):
        """ """
        super().__init__(database, parent)

        # Hook up confirm / cancel buttons
        self.confirmation_box.accepted.connect(self.handle_accept_new_employee)
        self.confirmation_box.rejected.connect(self.handle_reject_new_employee)

    @property
    def template_path(self) -> pathlib.Path:
        """Path to the .ui file to render this widget with."""

        with resources.path(
            "financial_management_system.templates", "add_employee.ui"
        ) as template:
            return template

    def show_warning(
        self,
        message: str = "Something went wrong",
        text: str = "Error",
        title: str = "Error",
    ) -> None:
        """Show a warning to the user."""

        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setInformativeText(message)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()

    def handle_accept_new_employee(self) -> None:
        """Parse user input, and add a new employee to the database. Kicks off a table refresh."""

        # Ensure all input has been provided
        missing = False
        for line_edit in self.findChildren(QtWidgets.QLineEdit):
            if line_edit.text():
                line_edit.setStyleSheet("background-color: white;")
            else:
                line_edit.setStyleSheet("background-color: red;")
                missing = True

        if missing:
            self.show_warning("Not all required inputs provided!")
            return

        # get user inputted values
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        city = self.city_input.text()
        state = self.state_input.text()
        zip_code = self.zip_code_input.text()
        ssn = self.ssn_input.text()
        withholdings = self.withholdings_input.text()
        salary = self.salary_input.text()

        # convert withholdings to float
        try:
            withholdings = float(withholdings)
        except:
            self.withholdings_input.setStyleSheet("background-color: red;")
            self.show_warning("Could not convert withholdings to float!")
            return

        # convert salary to float
        try:
            salary = float(salary)
        except:
            self.salary_input.setStyleSheet("background-color: red;")
            self.show_warning("Could not convert salary to float!")
            return

        # Attempt to add the new employee to the database
        try:
            self.database.add_employee(
                Employee(
                    first_name,
                    last_name,
                    city,
                    state,
                    zip_code,
                    ssn,
                    withholdings,
                    salary,
                )
            )
        except Exception as ex:
            self.show_warning(
                f"Could not add '{first_name} {last_name}' to the database: {ex}"
            )
            return

        # Re-render the table
        self.parent().refresh_table()

        # Close employee adding window
        self.close()

    def handle_reject_new_employee(self) -> None:
        """Cancels adding a new employee."""

        self.close()


class EmployeeManagementWindow(base_window.BaseWindow):
    """ """

    def __init__(
        self, database: MainDatabase, parent: typing.Optional[QtWidgets.QWidget] = None
    ):
        """ """
        super().__init__(database, parent)

        # Make table select by rows instead of by cells
        self.employee_table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        # Set up buttons
        self.add_employee_button.clicked.connect(self.handle_add_employee_click)
        self.remove_employee_button.clicked.connect(self.handle_remove_employee_click)

        # Set up child pages
        self.add_employee_window = None

        # Table state
        self.table_employees = []
        self.refresh_table()

    @property
    def template_path(self) -> pathlib.Path:
        """Path to the .ui file to render this widget with."""

        with resources.path(
            "financial_management_system.templates", "employee_management.ui"
        ) as template:
            return template

    def refresh_table(self) -> None:
        """Re-render the table based on contents of database"""

        self.table_employees = self.database.employees
        self.employee_table.setRowCount(len(self.table_employees))
        for idx, employee in enumerate(self.table_employees):
            for attr_idx, attr in enumerate(employee.table_attributes):
                self.employee_table.setItem(
                    idx, attr_idx, QtWidgets.QTableWidgetItem(str(attr))
                )

    #########################
    # Handle Button Presses #
    #########################

    def handle_add_employee_click(self) -> None:
        """ """

        self.add_employee_window = AddEmployeeWindow(
            database=self.database, parent=self
        )
        self.add_employee_window.show()

    def handle_remove_employee_click(self) -> None:
        """ """

        # Get row indices for all selected table contents
        selected_rows = set(
            [selection.row() for selection in self.employee_table.selectedIndexes()]
        )

        # Get corresponding employee objects for selected table contents
        selected_employees = [self.table_employees[idx] for idx in selected_rows]

        # Remove each employee from the database
        for selected_employee in selected_employees:
            self.database.remove_employee(selected_employee.employee_id)

        # Re-render the table
        self.refresh_table()

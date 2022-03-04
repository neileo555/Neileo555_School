from PyQt5 import uic, QtWidgets

import pathlib
import pandas as pd


class UiEmployee(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(UiEmployee, self).__init__(parent)
        uic.loadUi(self.template_path, self)
        self.loadData()
        self.returnEmpl.clicked.connect(self.retEmpl)
        self.show()

    @property
    def template_path(self) -> pathlib.Path:
        """ """

        return pathlib.Path(__file__).parent.parent / "templates/FinMngrEmployee.ui"

    def retEmpl(self):
        self.close()

    def addEmpl(dataF, listF):
        for i in range(len(listF)):
            dataF[i].append(listF[i])
        # add employee to dataframe

    #    def remEmpl(dataF):
    # remove employee from dataframe

    def loadData(self):
        dfEmployee = pd.DataFrame(
            {
                "firstName": ["Neil", "Drake", "Jonas"],
                "lastName": ["Chiruvella", "Eidukas", "Giver"],
                "city": ["LA", "Marina", "Paradise"],
                "state": ["CA", "CA", "NA"],
                "zip": ["90292", "90292", "23534"],
                "ssn": ["XXX-XXX-XXXX", "YYY-YYY-YYYY", "ZZZ-ZZZ-ZZZZ"],
                "wholding": ["0", "0", "0"],
                "salary": ["$100,000", "$125,000", "$100"],
            }
        )
        self.employeeTable.setRowCount(len(dfEmployee))
        for row in range(dfEmployee.shape[0]):
            for col in range(dfEmployee.shape[1]):
                self.employeeTable.setItem(
                    row,
                    col,
                    QtWidgets.QTableWidgetItem(dfEmployee[dfEmployee.columns[col]][row]),
                )


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        """ """

        super().__init__(parent)

        uic.loadUi(self.template_path, self)

        self.pushButton.clicked.connect(self.EmplClick)
        self.show()

    @property
    def template_path(self) -> pathlib.Path:
        """ """

        return pathlib.Path(__file__).parent.parent / "templates/FinMngrMainWin.ui"

    def EmplClick(self):
        self = UiEmployee(self)
        self.show()

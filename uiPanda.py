from turtle import width
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

import pandas as pd
import sys

class UiEmployee(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(UiEmployee, self).__init__(parent)
        uic.loadUi('FinMngrEmployee.ui', self)
        self.loadData()
        self.returnEmpl.clicked.connect(self.retEmpl)
        self.show()

    def retEmpl(self):
        self.close()

    def addEmpl(dataF,listF):
        for i in range(len(listF)):
            dataF[i].append(listF[i])
        # add employee to dataframe

#    def remEmpl(dataF):
        # remove employee from dataframe

    def loadData(self):
        dfEmployee = pd.DataFrame({'firstName': ['Neil', 'Drake', 'Jonas'],
                            'lastName': ['Chiruvella', 'Eidukas', 'Giver'],
                            'city': ['LA', 'Marina', 'Paradise'],
                            'state': ['CA', 'CA', 'NA'],
                            'zip': ['90292', '90292', '23534'],
                            'ssn': ['XXX-XXX-XXXX', 'YYY-YYY-YYYY', 'ZZZ-ZZZ-ZZZZ'],
                            'wholding': ['0', '0', '0'],
                            'salary': ['$100,000', '$125,000', '$100']})
        self.employeeTable.setRowCount(len(dfEmployee))
        for row in range(dfEmployee.shape[0]):
            for col in range(dfEmployee.shape[1]):
                self.employeeTable.setItem(row, col, QtWidgets.QTableWidgetItem(dfEmployee[dfEmployee.columns[col]][row]))
    
class UiMain(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(UiMain, self).__init__(parent)
        uic.loadUi('FinMngrMainWin.ui', self)
        self.pushButton.clicked.connect(self.EmplClick)
        self.show()

    def EmplClick(self):
        self = UiEmployee(self)      
        self.show()

# main
app = QApplication(sys.argv)
# window = UiEmployee()
window = UiMain()
window.show()

# window.pushButton.clicked.connect(lambda: print('List Employees'))
# window.pushButton_2.clicked.connect(lambda: print('Add Employees'))
# window.pushButton_3.clicked.connect(lambda: print('List Vendors'))
# window.pushButton_4.clicked.connect(lambda: print('Add Vendors'))
# window.pushButton_5.clicked.connect(lambda: print('List Customers'))
# window.pushButton_6.clicked.connect(lambda: print('Add Customers'))
# window.pushButton_7.clicked.connect(lambda: print('Pay Employee'))
# window.pushButton_8.clicked.connect(lambda: print('Payroll'))
# window.pushButton_9.clicked.connect(lambda: print('Inventory'))
# window.pushButton_10.clicked.connect(lambda: print('Create Invoice'))
# window.pushButton_11.clicked.connect(lambda: print('Invoice History'))
# window.pushButton_12.clicked.connect(lambda: print('Create PO'))
# window.pushButton_13.clicked.connect(lambda: print('PO History'))
# window.pushButton_14.clicked.connect(lambda: print('Balance Sheet'))
# window.pushButton_15.clicked.connect(lambda: print('Income Statement'))

try:
    sys.exit(app.exec_())
except:
    print("Exiting")


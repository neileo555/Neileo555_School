from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

import sys

class UiMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiMain, self).__init__()
        uic.loadUi('FinMngrMainWin.ui', self)
        self.show()

# class UiEmployee(QDialog):
class UiEmployee(QtWidgets.QTableWidget):
    def __init__(self):
        super(UiEmployee, self).__init__()
        uic.loadUi('FinMngrEmployee.ui', self)
        self.loadData()
        self.show()

    def loadData(self):
        ep1 = [{"firstName":'Neil',"lastName":'Chiruvella','city':'LA','state':'CA','zip':'90292','ssn':'XXX-XXX-XXXX','wholding':'0','salary':'$100,000'},
        {"firstName":'il',"lastName":'Chi','city':'LA','state':'CA','zip':'90292','ssn':'XXX-YYY-XXXX','wholding':'0','salary':'$140,000'}]
        row = 0
        #import pdb
        #pdb.set_trace()
        self.employeeTable.setRowCount(len(ep1))
        for employee in ep1:
            self.employeeTable.setItem(row,0, QtWidgets.QTableWidgetItem(employee['firstName']))
            self.employeeTable.setItem(row,1, QtWidgets.QTableWidgetItem(employee['lastName']))
            self.employeeTable.setItem(row,2, QtWidgets.QTableWidgetItem(employee['city']))
            self.employeeTable.setItem(row,3, QtWidgets.QTableWidgetItem(employee['state']))
            self.employeeTable.setItem(row,4, QtWidgets.QTableWidgetItem(employee['zip']))
            self.employeeTable.setItem(row,5, QtWidgets.QTableWidgetItem(employee['ssn']))
            self.employeeTable.setItem(row,6, QtWidgets.QTableWidgetItem(employee['wholding']))
            self.employeeTable.setItem(row,7, QtWidgets.QTableWidgetItem(employee['salary']))
            row+=1

# main
app = QApplication(sys.argv)
window = UiEmployee()
# window = UiMain()
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


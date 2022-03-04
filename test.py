# import sys

# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtWidgets import QLabel
# from PyQt5.QtWidgets import QPushButton
# from PyQt5.QtWidgets import QWidget
# from PyQt5 import uic

# app = QApplication(sys.argv)

# window = QWidget()
# window.setWindowTitle('Financial Statement Management')
# window.setGeometry(100, 100, 280, 200)
# window.move(825, 350)
# finLbl = QLabel('<h1>Main Menu</h1>', parent=window)
# finMng = QPushButton('Income Statement', parent=window)
# finLbl.move(70, 0)
# finMng.move(85, 150)

# window.show()

# sys.exit(app.exec_())

import pandas as pd

df = pd.DataFrame({'firstName': ['Neil', 'Drake', 'Jonas'],'lastName': ['Chiruvella', 'Eidukas', 'Giver'],
                    'city': ['LA', 'Marina', 'Paradise'],
                    'state': ['CA', 'CA', 'NA'],
                    'zip': ['90292', '90292', '23534'],
                    'ssn': ['XXX-XXX-XXXX', 'YYY-YYY-YYYY', 'ZZZ-ZZZ-ZZZZ'],
                    'wholding': ['0', '0', '0'],
                    'salary': ['$100,000', '$125,000', '$100']})

print(df)
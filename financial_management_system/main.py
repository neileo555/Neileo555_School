from PyQt5 import QtWidgets
from windows import main_window
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = main_window.UiEmployee()
    window = main_window.MainWindow()
    window.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")


if __name__ == "__main__":
    main()

from PyQt5.QtWidgets import QMainWindow, QApplication
from FormatadorCSV import *


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = FormatadorCSV()
    novo.show()
    qt.exec_()

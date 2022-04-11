import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from FormatCSV import FormatCSV

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = FormatCSV()
    novo.show()
    sys.exit(qt.exec_())

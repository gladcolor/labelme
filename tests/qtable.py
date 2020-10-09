import sys
from qtpy import QtCore
from qtpy.QtCore import Qt
from qtpy import QtGui
from qtpy import QtWidgets

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLabel, QCheckBox
from PyQt5.QtWidgets import *

lista = ['r1c1', 'r1c2', 'r1c3']
listb = ['r2c1', 'r2c2', 'r1c3']
listc = ['r3c1', 'r3c2', 'r3c3']
mystruct = {'row1':lista, 'row2':listb, 'row3':listc}

class MyTable(QTableWidget):
    def __init__(self, thestruct, *args):
        QTableWidget.__init__(self, *args)
        self.data = thestruct
        n = 0
        for key in self.data:
            m = 0
            for item in self.data[key]:
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
                m += 1
            n += 1
        self.itemSelectionChanged.connect(self.print_row)

    def print_row(self):
        items = self.selectedItems()
        print(str(items[0].text()))

def main(args):
    app = QApplication(args)
    table = MyTable(mystruct, 3, 3)
    table.show()

    sys.exit(app.exec_())

if __name__=="__main__":
    main(sys.argv)
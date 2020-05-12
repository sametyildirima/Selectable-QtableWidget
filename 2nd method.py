from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # use the custom context menu policy for the table widget, so that we can
        # connect the menu request to a slot
        self.table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.showTableMenu)

    def showTableMenu(self, pos):
        # get the text of the index at the mouse cursor (if any)
        text = self.table.indexAt(pos).data()
        menu = QtWidgets.QMenu()
        copyAction = menu.addAction('Copy')
        if not text:
            copyAction.setEnabled(False)
        # show the menu
        res = menu.exec_(QtGui.QCursor.pos())
        if res == copyAction:
            # if the menu has been triggered by the action, copy to the clipboard
            QtWidgets.QApplication.clipboard().setText(text)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
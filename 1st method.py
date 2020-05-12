from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # install an event filter on the table widget, so that we can filter all
        # its event, including keyboard presses
        self.table.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress and event == QtGui.QKeySequence.Copy:
            # check if an index is currently selected and it has text
            text = self.table.currentIndex().data()
            if text:
                # copy that text to the clipboard
                QtWidgets.QApplication.clipboard().setText(text)
        return super().eventFilter(source, event)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
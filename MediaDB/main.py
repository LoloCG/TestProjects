import sys
print("Running app")
from PySide6 import QtWidgets
from widgets import MainWindow

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

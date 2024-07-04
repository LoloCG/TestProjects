import sys
from PySide6 import QtWidgets
from widgets import MainWindow

print("Running app")
app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

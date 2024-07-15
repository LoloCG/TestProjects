import sys
print("Running app")
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSettings
from widgets import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')

    # Initialize settings
    settings = QSettings("MediaDatabaseApp", "AppSettings")

    window = MainWindow(settings)
    window.show()
    sys.exit(app.exec()) # Using sys.exit() is considered good practice because it ensures the application exits cleanly and any necessary cleanup is performed
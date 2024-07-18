import sys
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import (
        QMainWindow, QApplication
)
from UI_files.UI_MainWindow import Ui_MainWindow

# pyside6-rcc MW_Resources.qrc -o MW_Resources_rc.py

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("TestSidebar")

        # Set the initial page to the Home page
        self.ui.stackedWidget.setCurrentIndex(0)

        # Set initial state of the sidebar
        self.ui.SideMenuQWidget.setVisible(False)
        self.ui.SideIconQWidget.setHidden(False)

        # Connect buttons to pages
        self.ui.HomeSideButton.toggled.connect(self.HomePage_Called)
        self.ui.HomeSideButton2.toggled.connect(self.HomePage_Called)
        self.ui.GraphSideButton.toggled.connect(self.GraphPage_Called)
        self.ui.GraphSideButton2.toggled.connect(self.GraphPage_Called)
        self.ui.SpendsSideButton2.toggled.connect(self.SpendsPage_Called)
        self.ui.SpendsSideButton2.toggled.connect(self.SpendsPage_Called)

    def HomePage_Called(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def SpendsPage_Called(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def GraphPage_Called(self):
        self.ui.stackedWidget.setCurrentIndex(2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
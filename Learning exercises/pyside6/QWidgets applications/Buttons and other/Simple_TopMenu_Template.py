import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStatusBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Top FileMenu test")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create the buttons before the menu bar is created
        button_action = QAction("Button 1", self)
        button_action.setStatusTip("This is button 1")
        button_action.setCheckable(True) #Used when you want permanent check of the button
        button_action.triggered.connect(self.ButtonClick1)

        button_action2 = QAction("Button 2", self)
        button_action2.setStatusTip("For Button 2")
        button_action2.triggered.connect(self.ButtonClick2)

        # Create the menu bar and add the buttons
        menu = self.menuBar()

        file_menu = menu.addMenu("File")
        file_menu.addAction(button_action)

        # file_menu.addSeparator() # Used when you want separation between buttons

        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)

        # this is used to show the status tip when hovering over the button
        self.setStatusBar(QStatusBar(self))

    def ButtonClick1(self):
        print("button 1 clicked")

    def ButtonClick2(self):
        print("button 2 clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

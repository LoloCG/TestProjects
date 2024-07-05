# not working at the moment. Update in the future after more learning
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QStatusBar, QStackedWidget, QVBoxLayout,
    QPushButton
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Media Db")
        self.setMinimumSize(QSize(220, 330))

        # Initialize QStackedWidget
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Create main menu widget
        self.main_menu_widget = QWidget()
        self.stack.addWidget(self.main_menu_widget)
        main_menu_layout = QVBoxLayout(self.main_menu_widget)

        # Add buttons to main screen
        self.GoToQuery_Button = QPushButton("Add new Media")
        main_menu_layout.addWidget(self.GoToQuery_Button)
        self.GoToQuery_Button.clicked.connect(self.show_Query)

        # Create the buttons before the topmenu bar is created
        LightMode_TopMenu_Button = QAction("Light mode", self)
        LightMode_TopMenu_Button.setStatusTip("Change to Light theme with white background")
        LightMode_TopMenu_Button.triggered.connect(self.ButtonClick1)

        DarkMode_TopMenu_Button = QAction("Dark mode", self)
        DarkMode_TopMenu_Button.setStatusTip("Change to Dark theme with black background")
        DarkMode_TopMenu_Button.triggered.connect(self.ButtonClick2)

        # Create the menu bar and add the buttons
        menu = self.menuBar()

        file_menu = menu.addMenu("Settings")

        file_submenu = file_menu.addMenu("Themes")
        file_submenu.addAction(DarkMode_TopMenu_Button)
        file_submenu.addAction(LightMode_TopMenu_Button)

        # this is used to show the status tip when hovering over the button
        self.setStatusBar(QStatusBar(self))

        # Variable to keep track of dynamically created widgets
        self.current_widget = None

    def show_main_menu(self):
        # Remove current widget if it exists
        if self.current_widget:
            self.stack.removeWidget(self.current_widget)
            self.current_widget.deleteLater()
            self.current_widget = None
        # Show the main menu widget
        self.stack.setCurrentWidget(self.main_menu_widget)

    def show_Query(self):
        from Query import QueryWindow  # Import dynamically
        self.current_widget = QueryWindow(self)
        self.stack.addWidget(self.current_widget)
        self.stack.setCurrentWidget(self.current_widget)

    def ButtonClick1(self):
        print("Light mode button clicked")

    def ButtonClick2(self):
        print("Dark mode button clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

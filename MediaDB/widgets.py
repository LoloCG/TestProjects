from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QMainWindow
from PySide6.QtGui import QStandardItemModel, QStandardItem

from Widgets.UI_MWindow import Ui_MainAppWindow
from Widgets.UI_VideoQuery import Ui_VideoForm
from Widgets.UI_AboutWindow import Ui_AboutDialog
from data_handler import get_data, populate_table

class MainWindow(QMainWindow, Ui_MainAppWindow): # QMainWindow is required instead of QWidget, as setCentralWidget is part of the first one.
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Media Database")

        self.VideoQueryMenuButton.triggered.connect(self.ShowVideoQuery)
        self.AboutMenuButton.triggered.connect(self.ShowAboutDialog)
        self.SearchButton.clicked.connect(self.searchfunct)
        self.PrintSelectedButton.clicked.connect(self.InfoSelectedItem)

        
        DBdata = get_data() # obtains the data that will be displayed in the table

        # calls the function introducing the data to the database.
            # function uses two variables. The object and the data that will be used.
        populate_table(self.MainTableWidget, DBdata)

    # function to find in db from MWindows
    def searchfunct(self):
        search_text = self.SearchLineEdit.text()
        print("Searching for:",search_text, "in db") 
    
    # function to print info of the selected item in the db
    def InfoSelectedItem(self):
        selected_items = self.MainTableWidget.selectedItems()
        if not selected_items:
            print("No item selected")
            return
    
        row = selected_items[0].row()
        row_data = []
        for column in range(self.MainTableWidget.columnCount()):
            item = self.MainTableWidget.item(row, column)
            row_data.append(item.text() if item else "")
    
        print("Info of selected film: ")
        print(f"Name: {row_data[0]}, Type: {row_data[1]}, Recommended by: {row_data[2]}, Tags: {row_data[3]}")

    # Functions to show different windows
    def ShowVideoQuery(self):
        print("showing video query")
        self.video_query_window = VideoQuery()
        self.video_query_window.show()
        self.video_query_window.raise_()  # Bring the window to the front

    def ShowAboutDialog(self):
        print("Showing About Dialog")
        self.Show_About_Dialog = AboutDialog()
        self.Show_About_Dialog.show()
        self.Show_About_Dialog.raise_()

class VideoQuery(QWidget, Ui_VideoForm):
       def __init__(self):
        super().__init__()
        self.setupUi(self) 
        #self.setWindowTitle("Video Query"
        self.CancelButton.clicked.connect(self.close)


class AboutDialog(QWidget, Ui_AboutDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.AboutAcceptButton.clicked.connect(self.close)
    
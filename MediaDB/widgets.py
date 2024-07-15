from PySide6.QtCore import Qt, QSettings
from PySide6.QtWidgets import (
        QWidget, QMainWindow, QTableWidgetItem, 
        QHeaderView, QMessageBox
)
from UI_files.UI_MWindow import Ui_MainAppWindow
from UI_files.UI_VideoQuery import Ui_VideoForm
from UI_files.UI_AboutWindow import Ui_AboutDialog

from Themes.themes import Palettes

from data_handler import (
    get_data, insert_data, get_media_types, delete_data
)

class MainWindow(QMainWindow, Ui_MainAppWindow): # QMainWindow is required instead of QWidget, as setCentralWidget is part of the first one.
    def __init__(self, settings):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Media Database")
        
        self.settings = settings
        self.load_settings()

        self.VideoQueryMenuButton.triggered.connect(self.ShowVideoQuery)
        self.AddNewButton.clicked.connect(self.ShowVideoQuery)
        self.AboutMenuButton.triggered.connect(self.ShowAboutDialog)
        self.SearchButton.clicked.connect(self.searchfunct)
        self.PrintSelectedButton.clicked.connect(self.InfoSelectedItem)
        self.Delete_selectedMenuButton.triggered.connect(self.DeleteItem)
        
        self.DarkThemeAction.triggered.connect(self.SelectedTheme)
        self.LightThemeAction.triggered.connect(self.SelectedTheme)
        self.NeonThemeAction.triggered.connect(self.SelectedTheme)
        self.theme_action_group = [self.DarkThemeAction, self.LightThemeAction, self.NeonThemeAction]

        DBdata = get_data() 
        # calls the function introducing the data to the database.
            # function uses two variables. The object and the data that will be used.
        self.populate_table(self.MainTableWidget, DBdata)

    def load_settings(self):
        theme = self.settings.value("theme", "light")
        if theme == "dark":
            self.DarkThemeAction.setChecked(True)
            self.setPalette(Palettes.dark_palette())
        elif theme == "neon":
            self.NeonThemeAction.setChecked(True)
            self.setPalette(Palettes.neon_palette())
        else:
            self.LightThemeAction.setChecked(True)
            self.setPalette(Palettes.light_palette())

    def save_settings(self, theme):
        self.settings.setValue("theme", theme)

    def SelectedTheme(self):
        sender = self.sender()

        if sender == self.DarkThemeAction:
            self.setPalette(Palettes.dark_palette())
            self.save_settings("dark")
        elif sender == self.LightThemeAction:
            self.setPalette(Palettes.light_palette())
            self.save_settings("light")
        elif sender == self.NeonThemeAction:
            self.setPalette(Palettes.neon_palette())
            self.save_settings("neon")

        # Ensure only the triggered action is checked
        for action in self.theme_action_group:
            action.setChecked(action == sender)

    def populate_table(self, table_widget, data): # Obtains the data from the DB to show it in the table of main window
        if not data:
            print("No data to display.")
            table_widget.setRowCount(0)
            return
                
        print("populating table with ", len(data), " rows and ", len(data[0]), "columns")
        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(len(data[0]))
        table_widget.setHorizontalHeaderLabels(["id", "Name", "Type", "Recommended by", "Tags"])

        # Center the header text
        header = table_widget.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setSectionResizeMode(QHeaderView.Stretch) # Adjust column widths to stretch and cover the entire table width

        for row_index, row_data in enumerate(data):
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(row_data[col_index])) # Ensure data is converted to string
                #item = QTableWidgetItem(cell_data) # This code is similar to above, but the data is not converted to string. Using it causes id for item deletion, etc. not functional            
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Make the item non-editable 
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the item text
                table_widget.setItem(row_index, col_index, item)

        table_widget.setColumnHidden(0, True)  # Hide the ID column

    # function to find in db from MWindows
        # not finished yet. Does nothing at the moment.
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
        
        # TODO: make it so that when its empty it is not printed at all or says none
        print("Info of selected film: ")
        print(f"ID: {row_data[0]}")
        print(f"Name: {row_data[1]}")
        print(f"Type: {row_data[2]}")
        print(f"Recommended by: {row_data[3]}")
        print(f"Tags: {row_data[4]}")

    def DeleteItem(self):
        selected_items = self.MainTableWidget.selectedItems()
        if not selected_items:
            print("No item selected")
            return

        row = selected_items[0].row()
        item = self.MainTableWidget.item(row, 0)
        item_id = item.text()
        #print("item ID to be deleted:", item_id)

        delete_data(item_id)
        
        # Refreshes the table in main windows before going back to it
        DBdata = get_data()
        self.populate_table(self.MainTableWidget, DBdata)

    # Functions to show different windows
    def ShowVideoQuery(self):
        print("showing video query")
        self.video_query_window = VideoQuery(self, self.MainTableWidget) #Requires the passing self to the VideoQuery constructorof & the table widget 
        self.video_query_window.show()
        self.video_query_window.raise_()  # Bring the window to the front

    def ShowAboutDialog(self):
        print("Showing About Dialog")
        self.Show_About_Dialog = AboutDialog()
        self.Show_About_Dialog.show()
        self.Show_About_Dialog.raise_()

class VideoQuery(QWidget, Ui_VideoForm):
    def __init__(self, main_window, table_widget):
        super().__init__()
        self.setupUi(self) 
        self.main_window = main_window  # Store the reference to the MainWindow instance
        self.table_widget = table_widget

        self.populate_type_combobox()
        
        self.CancelButton.clicked.connect(self.close)
        self.ApplySubmitButton.clicked.connect(self.ApplySubmit_Item)
        self.AcceptSubmitButton.clicked.connect(self.AcceptSubmit_Item)

    def ApplySubmit_Item(self):
        self.Submit_Item(False)  # Call Submit_Item with False

    def AcceptSubmit_Item(self):
        self.Submit_Item(True)  # Call Submit_Item with True

    def Submit_Item(self, CloseBool):
        name = self.Name_LineEdit.text()
        media_type = self.Type_ComboBox.currentText()
        recommendation = self.Recommendation_LineEdit.text()
        tags = self.Tags_LineEdit.text()

        if not name or not media_type:
            print("Name and media type fields required")
            ret = QMessageBox.information(self, "Data entry error", "Fields \"Name\" and \"Type\" are required",
                                    QMessageBox.Ok | QMessageBox.Cancel)
            if ret == QMessageBox.Ok:
                print("User chose OK")
            else:
                print("User chose Cancel")
            return

        item_info = [name, media_type, recommendation, tags]
        insert_data(item_info)

        # Refresh the table in the main window
        DBdata = get_data()
        self.main_window.populate_table(self.table_widget, DBdata)

        # Clear the input fields after submission
        self.Name_LineEdit.clear()
        self.Type_ComboBox.setCurrentIndex(0)
        self.Recommendation_LineEdit.clear()
        self.Tags_LineEdit.clear()

        if CloseBool:
            self.close()
        else: 
            self.populate_type_combobox()

    def populate_type_combobox(self):
        types = get_media_types()
        self.Type_ComboBox.addItems(types)

class AboutDialog(QWidget, Ui_AboutDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.AboutAcceptButton.clicked.connect(self.close)

import random

from PySide6.QtCore import Qt, QSettings
from PySide6.QtWidgets import (
        QWidget, QMainWindow, QTableWidgetItem, QApplication,
        QHeaderView, QMessageBox
)
from UI_files.UI_MWindow import Ui_MainAppWindow
from UI_files.UI_VideoQuery import Ui_VideoForm
from UI_files.UI_AboutWindow import Ui_AboutDialog
from UI_files.UI_ItemInfo import Ui_ItemInfoWidget

from Themes.themes import Palettes

from data_handler import (
    get_alldata, insert_data, get_media_types, delete_data, get_itemdata, update_data
)

class MainWindow(QMainWindow, Ui_MainAppWindow): # QMainWindow is required instead of QWidget, as setCentralWidget is part of the first one.
    def __init__(self, settings):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Media Database")
        
        self.settings = settings
        self.load_settings()

        self.AboutMenuButton.triggered.connect(self.ShowAboutDialog)
        self.Show_RandomButton.clicked.connect(self.ShowRandom)

        # Buttons related to the table
        self.VideoQueryMenuButton.triggered.connect(self.ShowVideoQuery)
        self.AddNewButton.clicked.connect(self.ShowVideoQuery)
        self.Delete_selectedMenuButton.triggered.connect(self.DeleteItem)
        self.InfoSelectedButton.clicked.connect(self.InfoSelectedItem)
        self.EditSelectedButton.clicked.connect(self.EditInQuery)

        # Buttons about settings
        self.DarkThemeAction.triggered.connect(self.SelectedTheme)
        self.LightThemeAction.triggered.connect(self.SelectedTheme)
        self.NeonThemeAction.triggered.connect(self.SelectedTheme)
        self.theme_action_group = [self.DarkThemeAction, self.LightThemeAction, self.NeonThemeAction]

        DBdata = get_alldata() 
        # calls the function introducing the data to the database.
            # function uses two variables. The object and the data that will be used.
        self.populate_table(self.MainTableWidget, DBdata)

        # Connect search field
        self.SearchLineEdit.textChanged.connect(self.searchfunct)
# Settings functions
    def load_settings(self):
        theme = self.settings.value("theme", "light")
        if theme == "dark":
            self.DarkThemeAction.setChecked(True)
            self.set_global_palette(Palettes.dark_palette())
        elif theme == "neon":
            self.NeonThemeAction.setChecked(True)
            self.set_global_palette(Palettes.neon_palette())
        else:
            self.LightThemeAction.setChecked(True)
            self.set_global_palette(Palettes.light_palette())

    def save_settings(self, theme):
        print("saving settings")
        self.settings.setValue("theme", theme)

# Palette functions
    def SelectedTheme(self):
        sender = self.sender()

        if sender == self.DarkThemeAction:
            self.set_global_palette(Palettes.dark_palette())
            self.save_settings("dark")
        elif sender == self.LightThemeAction:
            self.set_global_palette(Palettes.light_palette())
            self.save_settings("light")
        elif sender == self.NeonThemeAction:
            self.set_global_palette(Palettes.neon_palette())
            self.save_settings("neon")

        # Ensure only the triggered action is checked
        for action in self.theme_action_group:
            action.setChecked(action == sender)

    def set_global_palette(self, palette):
        QApplication.instance().setPalette(palette) # It applies the palette to the application level, rather than window level only.

    def populate_table(self, table_widget, data): # Obtains the data from the DB to show it in the table of main window
        if not data:
            #print("No data to display.")
            table_widget.setRowCount(0)
            return
                
        #print("populating table with ", len(data), " rows and ", len(data[0]), "columns")
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

    def searchfunct(self): # Searches items in the DB based on the SearchLineEdit and SearchByComboBox objects. Sends to populate_table to only show these 
        search_text = self.SearchLineEdit.text().lower()
        search_column = self.SearchByComboBox.currentText()

        # TODO: This is hardcoded ATM, Maybe in the future make it more dynamic
        column_map = {
            "Name": 1,
            "Type": 2,
            "Recommended By": 3,
            "Tags": 4
        }

        data = get_alldata()

        if search_column in column_map:
            column_index = column_map[search_column]
            filtered_data = [row for row in data if search_text in row[column_index].lower()]
        else:
            filtered_data = data  # Default to all data if column not found

        self.populate_table(self.MainTableWidget, filtered_data)

    def Current_Table_Items(self): # Retrieves all the items that are displayed in the table.
        row_count = self.MainTableWidget.rowCount()
        column_count = self.MainTableWidget.columnCount()

        current_data = []

        for row in range(row_count):
            row_data = []
            for column in range(column_count):
                item = self.MainTableWidget.item(row, column)
                row_data.append(item.text() if item else "")
            current_data.append(row_data)

        return current_data

    def ShowRandom(self): # Selects a random item from the current table
        current_data = self.Current_Table_Items() 
        
        if current_data:
            current_data_id = [row[0] for row in current_data] # Uses a list comprehension to create a list of the IDs from each row 
            random_id = random.choice(current_data_id)  # Select a random item from the current data
            
            item_data = get_itemdata(random_id)
            
            item_data_dict = {  
            "name": item_data[0],  
            "type": item_data[1],
            "recommended": item_data[2],
            "tags": item_data[3]
        }
            
            self.Show_ItemInfo_Widget = ItemInfoWidget(item_data_dict)
            self.Show_ItemInfo_Widget.show()
            self.Show_ItemInfo_Widget.raise_()

        else:   # TODO: show a warning window or sound to indicate invalid
            print("No data available to randomize.")
            return

    def InfoSelectedItem(self): # Prints all info of the selected item from the db to the terminal. 
        # TODO: make it use ItemInfoWidget for this
        selected_items = self.MainTableWidget.selectedItems()
        if not selected_items:
            print("No item selected")
            return
    
        row = selected_items[0].row()
        row_data = []
        for column in range(self.MainTableWidget.columnCount()):
            item = self.MainTableWidget.item(row, column)
            row_data.append(item.text() if item else "")

        item_data_dict = {
            "id": row_data[0],  
            "name": row_data[1],  
            "type": row_data[2],
            "recommended": row_data[3],
            "tags": row_data[4]
        }

        self.Show_ItemInfo_Widget = ItemInfoWidget(item_data_dict)
        self.Show_ItemInfo_Widget.show()
        self.Show_ItemInfo_Widget.raise_()

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
        DBdata = get_alldata()
        self.populate_table(self.MainTableWidget, DBdata)

    def EditInQuery(self):
        selected_items = self.MainTableWidget.selectedItems()
        
        if not selected_items:
            #print("No item selected")
            return
            
        row = selected_items[0].row()
        item_id = self.MainTableWidget.item(row, 0).text()

        #print(item_id)

        self.video_query_window = VideoQuery(self, self.MainTableWidget, item_id)
        self.video_query_window.show()
        self.video_query_window.raise_()  
        
# Functions to show different windows
    def ShowVideoQuery(self):
        print("showing video query")
        self.video_query_window = VideoQuery(self, self.MainTableWidget) #Requires the passing self to the VideoQuery constructorof & the table widget 
        self.video_query_window.show()
        self.video_query_window.raise_()  # Bring the window to the front

    def ShowAboutDialog(self):
        #print("Showing About Dialog")
        self.Show_About_Dialog = AboutDialog()
        self.Show_About_Dialog.show()
        self.Show_About_Dialog.raise_()

    #def ShowRandom(self):
class VideoQuery(QWidget, Ui_VideoForm):
    def __init__(self, main_window, table_widget, item_id=None):
        super().__init__()
        self.setupUi(self) 
        self.main_window = main_window  # Store the reference to the MainWindow instance
        self.table_widget = table_widget
        self.item_id = item_id

        self.populate_type_combobox()

        #print("id of item to edit:",item_id)

        if self.item_id:
            self.load_item_data()
            '''
            get_itemdata(item_id)

            self.Name_LineEdit.setText(item_data[0])
            self.Type_ComboBox.setCurrentText(item_data[1])
            self.Recommendation_LineEdit.setText(item_data[2])
            self.Tags_LineEdit.setText(item_data[3])
            '''

        self.CancelButton.clicked.connect(self.close)
        self.ApplySubmitButton.clicked.connect(self.ApplySubmit_Item)
        self.AcceptSubmitButton.clicked.connect(self.AcceptSubmit_Item)

    def load_item_data(self):
        item_data = get_itemdata(self.item_id)

        if item_data: # TODO: is this if really necessary?
            self.Name_LineEdit.setText(item_data[0])
            self.Type_ComboBox.setCurrentText(item_data[1])
            self.Recommendation_LineEdit.setText(item_data[2])
            self.Tags_LineEdit.setText(item_data[3])

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
            # TODO: maybe remove one of the two buttons
            print("Name and media type fields required")
            ret = QMessageBox.information(self, "Data entry error", "Fields \"Name\" and \"Type\" are required",
                                    QMessageBox.Ok | QMessageBox.Cancel)
            '''
            if ret == QMessageBox.Ok:
                print("User chose OK")
            else:
                print("User chose Cancel")
            '''
            return

        item_info = [name, media_type, recommendation, tags]

        if self.item_id:
            update_data(self.item_id, item_info)
        else:
            insert_data(item_info)

        DBdata = get_alldata()
        self.main_window.populate_table(self.table_widget, DBdata)

        self.clear_fields()

        if CloseBool:
            self.close()
        else:
            self.populate_type_combobox()

    def clear_fields(self):
        self.Name_LineEdit.clear()
        self.Type_ComboBox.setCurrentIndex(0)
        self.Recommendation_LineEdit.clear()
        self.Tags_LineEdit.clear()

    def populate_type_combobox(self):
        types = get_media_types()
        self.Type_ComboBox.addItems(types)

class AboutDialog(QWidget, Ui_AboutDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.AboutAcceptButton.clicked.connect(self.close)

class ItemInfoWidget(QWidget, Ui_ItemInfoWidget):
    def __init__(self,item_data):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

        # Populate the UI elements with the item data
        self.NameLineEditInfo.setText(item_data["name"])
        self.TypeLineEditInfo.setText(item_data["type"])
        self.ReccLineEditInfo.setText(item_data["recommended"])
        self.TagsLineEditInfo.setText(item_data["tags"])

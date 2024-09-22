# Shows a table widget with sample data, and a button to print the selected row into the terminal
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QTableView, QPushButton, QVBoxLayout
    )
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QMainWindow):  # We create a class, inheriting from QMainWindow
    def __init__(self): # The constructor
        super().__init__() 

        self.setWindowTitle("MainWindow App")

        central_widget = QWidget(self)  # Create a central widget that will contain other widgets
        self.setCentralWidget(central_widget)  # Set the central widget
        layout = QVBoxLayout(central_widget) # Create a vertical layout for the central widget

        # Create Table and button, then add them to the layout
        self.table = QTableView()
        button = QPushButton("Print to Terminal")
        layout.addWidget(self.table)
        layout.addWidget(button)
        
        # Connect button to its function
        button.clicked.connect(self.print_Row)     
        
        # this is the data that will be displayed in the table
        testdata = [
            ["T1A", "T1B"],
            ["T2A", "T2B"],
            ["T3A", "T3B"],
        ]

        model = QStandardItemModel() # Create a model for the table. It is what holds the data 
        model.setHorizontalHeaderLabels(["Column 1", "Column 2"]) # Set headers if needed

        for row in testdata:  # Iterate over each row in the testdata list
            # Create a list of QStandardItem objects, one for each cell in the row
            items = [QStandardItem(cell) for cell in row] #The list comprehension creates [QStandardItem("T1A"), QStandardItem("T1B")]. This list is appended to the model as a new row.
            # Append the list of QStandardItem objects as a new row in the model
            model.appendRow(items)


        self.table.setModel(model) # Set the model to the table


    def print_Row(self): #         Prints the data of the currently selected row to the terminal.
        selection_model = self.table.selectionModel()  # Get the selection model of the table
        selected_rows = selection_model.selectedRows()  # Get the selected rows

        for index in selected_rows:  # Iterate over the selected rows
            row_data = []
            for column in range(self.table.model().columnCount()):  # Iterate over the columns
                item = self.table.model().item(index.row(), column)  # Get the item in the current cell
                row_data.append(item.text())  # Append the item's text to the row data
            print(row_data)  # Print the row data to the terminal
 
app = QtWidgets.QApplication(sys.argv) # Create the application instance
window = MainWindow() # Create the main window instance
window.show() # Show the main window
app.exec()  # Enter the application main loop

from PySide6.QtWidgets import QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt
import sqlite3
import os

# Stores the supposed path for the database, which is the root directory of the script + the name of db
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media_database.db')

def setup_database():
    if not os.path.exists(db_path):
        print("Database not found, creating database at: ", db_path)
        
        # Connect to the database (this will create the file if it doesn't exist)
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS media (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            recommended_by TEXT,
            tags TEXT
        )
        ''')

        connection.commit()
        connection.close()

        print("DB created at: ", db_path)
        
    else:
        print("Database found at: ", db_path)

def get_data():
    
    print("Obtaining items from DB")

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute('SELECT name, type, recommended_by, tags FROM media')
    data = cursor.fetchall()
    
    connection.close()

def populate_table(table_widget, data):

    if not data:
        print("No data to display.")
        table_widget.setRowCount(0)
        table_widget.setColumnCount(4)
        table_widget.setHorizontalHeaderLabels(["Name", "Type", "Recommended by", "Tags"])
        return

    print("populating table with ", len(data), " rows and ", len(data[0]), "columns")
    table_widget.setRowCount(len(data))
    table_widget.setColumnCount(len(data[0]))
    #table_widget.setColumnCount(4)  # Ensure the column count matches your data schema    
    table_widget.setHorizontalHeaderLabels(["Name", "Type", "Recommended by", "Tags"])

    # Center the header text
    header = table_widget.horizontalHeader()
    header.setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
    # Adjust column widths to stretch and cover the entire table width
    header.setSectionResizeMode(QHeaderView.Stretch)

    for row_index, row_data in enumerate(data):
        for col_index, cell_data in enumerate(row_data):
            item = QTableWidgetItem(cell_data)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the item text
            table_widget.setItem(row_index, col_index, item)

# Run setup_database when the module is first imported
setup_database()


# Unused code

''' Was used to check if the database table was created correctly.
# Check if the table was created or already exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='media'")
if cursor.fetchone() is None:
    print("Error: Table 'media' was not created.")
else:
    print("Table 'media' is ready.")
'''
''' used in get_data function, used to return an empty list. Doesnt seem to be necessary
    if not data:
        print("No items found in the database.")
        return []
    return data
'''
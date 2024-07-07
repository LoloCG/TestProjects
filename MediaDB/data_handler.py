from PySide6.QtWidgets import QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt
import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, 'media_database.db')

def setup_database():
    print("Setting up database")

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
    
    # Optionally, insert initial data if the table is empty
    cursor.execute('SELECT COUNT(*) FROM media')
    if cursor.fetchone()[0] == 0:
        initial_data = [
            ("La teta asustada/The Milk of Sorrow", "Film", "John Doe", "Drama"),
            ("Song Without a Name/Canción sin nombre", "Film", "Jane Smith", "Drama"),
            ("Magallanes", "Film", "Robert Brown", "Drama"),
            ("The City and the Dogs", "Film", "Emily White", "Drama"),
        ]
        cursor.executemany('''
        INSERT INTO media (name, type, recommended_by, tags) VALUES (?, ?, ?, ?)
        ''', initial_data)

    connection.commit()
    connection.close()
    print("DB created at: ", db_path)

def get_data():
    
    print("obtaining data")
    
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute('SELECT name, type, recommended_by, tags FROM media')
    data = cursor.fetchall()
    
    connection.close()
    return data

    '''
    return [
        ["La teta asustada/The Milk of Sorrow", "Film"],
        ["Song Without a Name/Canción sin nombre", "Film"],
        ["Magallanes", "Film"],
        ["The City and the Dogs", "Film"],
    ]
    '''
def populate_table(table_widget, data):
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
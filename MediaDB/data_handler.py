from PySide6.QtWidgets import QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt

def get_data():
    print("obtaining data")
    return [
        ["La teta asustada/The Milk of Sorrow", "Film"],
        ["Song Without a Name/Canción sin nombre", "Film"],
        ["Magallanes", "Film"],
        ["The City and the Dogs", "Film"],
    ]

def populate_table(table_widget, data):
    print("populating table with ", len(data), " rows and ", len(data[0]), "columns")
    table_widget.setRowCount(len(data))
    table_widget.setColumnCount(len(data[0]))
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

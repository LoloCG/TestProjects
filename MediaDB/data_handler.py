#from PySide6.QtWidgets import QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt
import sqlite3
import os

# Stores the supposed path for the database, which is the root directory of the script + the name of db
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media_database.db')

def setup_database(): # Creates database if it doesnt exist
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

        print("DB created")
        
    else:
        print("Database found at: ", db_path)

def get_alldata(): # Obtains all the data from the database
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute('SELECT id, name, type, recommended_by, tags FROM media')

    data = cursor.fetchall()
    connection.close()

    return data

def get_itemdata(item_id):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute('SELECT name, type, recommended_by, tags FROM media WHERE id = ?', (item_id,))
    item_data = cursor.fetchone()
    connection.close()
    return item_data

def get_media_types(): # Obtains existing "types" from the database, to be used in type combobox in query
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute('SELECT DISTINCT type FROM media')
    types = cursor.fetchall()
    
    connection.close()
    return [type_[0] for type_ in types]  # Extract types from tuples

def insert_data(item_info): # Used to insert data (item_info) into DB

    print("inserting data:",item_info)

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute('''
    INSERT INTO media (name, type, recommended_by, tags) 
    VALUES (?, ?, ?, ?)
    ''', item_info)

    connection.commit()
    connection.close()

def delete_data(text_id): # Uses the item ID as string to search the item in DB and delete it   
    item_id = int(text_id)
    print("deleting item with ID:",item_id)

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute('''
    DELETE FROM media 
    WHERE id = ?
    ''', (item_id,))  # Pass item_id as a tuple. without the (), the code wont work well.
    
    connection.commit()
    connection.close()

def update_data(item_id, item_info):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute('''
    UPDATE media 
    SET name = ?, type = ?, recommended_by = ?, tags = ? 
    WHERE id = ?
    ''', (*item_info, item_id))

    connection.commit()
    connection.close()
    
setup_database() # Run setup_database when the module is first imported

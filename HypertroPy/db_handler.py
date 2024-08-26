import sys,os 

sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Databases\SQLite')
from MODULE_SQLite_functions import DatabaseHandler

main_db_name = 'main_db.db'
main_db_folder_dir = os.path.dirname(os.path.abspath(__file__))
main_db = DatabaseHandler(db_name=main_db_name, db_dir=main_db_folder_dir)
main_table_name = 'full_data'

def db_startup():
    if main_db.check_db_existance() is False:
        print("Database does not exist, setting it up:")

    else:
        print("Database exists")
        print("...")
        return

# db.setup_exer_cons_table(exer_list[0])

def setup_exer_cons_table(exer_obj):
    exer_cons_table_name = 'exer_cons_table'

    exer_obj_attr_dict = {}
    for itemName, item in exer_obj.__dict__.items():
        exer_obj_attr_dict[itemName] = item
    
    sql_dict = main_db.convert_dict_valType_to_sqlType(exer_obj_attr_dict)
    main_db.create_db_table(tableItems=sql_dict, mainTable_name=exer_cons_table_name)
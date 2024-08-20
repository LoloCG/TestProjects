import sys, os
import db_handler, hours_per_subject

def main_menu():
    option_list = [
        'Show hours per subject',
        'Show weekly hours studied'
    ]

    while True:
        # TODO: make it into a dynamic loop...
        print("\nMain Menu")
        print("1.", option_list[0])
        print("2.", option_list[1])
        print("3. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            menu_opt1()
        elif choice == '2':
            menu_opt2()
        elif choice == '3':
            print("Exiting the program.")
            return
        else:
            print("Invalid choice, please enter again.\n")

def menu_opt1():
    print()
    df = db_handler.retrieve_main_table() # TODO: make it so that dataframe does not need to be passed around so much, and instead is obtained directly from the database
    hours_per_subject.main(df)
    print("Returning to main menu...\n")

def menu_opt2():
    print()
    print("Option 2 not implemented yet...")

if __name__ == "__main__":
    print("\nRunning program")
    
    target_file_folder_dir = os.path.dirname(os.path.abspath(__file__)) 
    chosen_file = '3º FarmNutr TDL_Log.csv'
    db_handler.main(target_file_folder_dir, chosen_file)

    main_menu()

def oldcode():
    # ============= Modules import ==========
        # 
    sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Pandas')
        # MODULE_pandas_basic.py

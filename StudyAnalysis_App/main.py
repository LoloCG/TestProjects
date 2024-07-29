import os
import pandas as pd
import numpy as np
import sys

sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Pandas\Excel')
excel_ImpExp = __import__('module_excel_ImportExport_functs')

main_dir = os.path.dirname(os.path.abspath(__file__))

# df_raw = pd.read_csv(file_path, encoding='utf-16', delimiter='\t', skiprows=1)

def main():

    chosen_file = excel_ImpExp.select_excelFile_fromFolder(main_dir)

    file_path = os.path.join(main_dir, chosen_file) 
    
    df_raw = excel_ImpExp.CSV_file_to_df_bruteforce(file_path)
    print()
    print("n-dimensions of array:",df_raw.ndim)
    print()
    print("keys:",df_raw.keys())
    print()
    print(df_raw)

    '''
    encoding =  excel_ImpExp.detect_encoding(file_path)
    print("file encoding = ", encoding)
    rowstart = excel_ImpExp.detect_CSV_header_row(file_path)
    
    print()
    if chosen_file == "3º FarmNutr TDL_Log.csv" and rowstart == 0:
        print("FAIL")
    elif chosen_file == "test.csv" and rowstart == 1:
        print("FAIL")
    else:
        print("success?")
    '''
    '''
    # Seems that for the .csv of the Todolist, it requires the encoding and delimiter to be set as the following
    
    print("n-dimensions of array:")
    print(df_raw.ndim)
    print()
    print("keys:")
    print(df_raw.keys())
    print()
    print(df_raw)
        #print("values:")
        #print(df_raw.values())
    
    #df_raw = excel_ImpExp.CSV_file_to_df_encode(file_path)
    '''
    '''
    path_df = df_raw['tPath']
    #

    for data in path_df.items():
       print(data)
    '''
main()
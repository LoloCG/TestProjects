import os
import numpy as np
import sys

sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Pandas\Excel')
    # MODULE_pandas_excel_functions.py
sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Pandas')
    # MODULE_pandas_basic.py
    
from MODULE_pandas_basic import DataCleaner, DataFrameTransformer, DataPlotter
from MODULE_pandas_excel_functions import ExcelDataExtract

def main(raw_dataframe):
    df_clean = DataCleaner(raw_dataframe)
    df_clean.basic_raw_pretreatment()
    df_clean.convert_dataframe_dates(removeDateCol=False)
    df_clean.show_missing_files()

    ColToFilter = 'Period'
    FilterValues = ['1st semester', '2nd Semester']
    colsToGroup = ['Time Spent (Hrs)', 'Period', 'Subject']

    transformed_df = DataFrameTransformer(df_clean.dataframe)
    transformed_df.filter_df_column_by_val(ColToFilter,FilterValues) 
    transformed_df.multiIndex_group(colsToGroup)
    
    print(transformed_df.dataframe)

    df_plot = DataPlotter(transformed_df.dataframe)
    df_plot.identify_column_hierarchy()
    df_plot.plot_hierarchical_categorical_bar_chart()

def oldcode():
    # The following is already in main.py
    chosen_file = '3º FarmNutr TDL_Log.csv'
    sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Pandas\Excel')
    
    excelCSV_raw = ExcelDataExtract()
    excelCSV_raw.csv_to_dataframe(chosen_file)
    
    #DEBUG: print(f"in main, df from CSV type: {type(excelCSV_raw.dataframe)}")

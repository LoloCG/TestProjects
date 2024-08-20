import os
import numpy as np
import sys

sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Matplotlib')    
from MODULE_matplot_pandas import DataPlotter
sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Pandas')    
from MODULE_pandas_basic import DataCleaner, DataFrameTransformer
sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Pandas\Excel')
from MODULE_pandas_excel_functions import ExcelDataExtract

def main(dataframe):
    clean_dataframe = clean_dataframe_for_plotting(dataframe)

    print(f"Plotting data:\n{clean_dataframe}")
    df_plot = DataPlotter(clean_dataframe)
    df_plot.identify_column_hierarchy()
    df_plot.plot_hierarchical_categorical_bar_chart()

def clean_dataframe_for_plotting(dataframe):
    ColToFilter = 'Period'
    FilterValues = ['1st semester', '2nd Semester']
    colsToGroup = ['Time Spent (Hrs)', 'Period', 'Subject']
    
    transformed_df = DataFrameTransformer(dataframe)
    transformed_df.filter_df_column_by_val(ColToFilter,FilterValues) 
    transformed_df.multiIndex_group(colsToGroup)

    return transformed_df.dataframe

def oldcode():
    # The following is already in main.py
    chosen_file = '3º FarmNutr TDL_Log.csv'
    sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Pandas\Excel')
    
    excelCSV_raw = ExcelDataExtract()
    excelCSV_raw.csv_to_dataframe(chosen_file)
    
    #DEBUG: print(f"in main, df from CSV type: {type(excelCSV_raw.dataframe)}")
    r'''
    sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Matplotlib')
    import MODULE_matplot_pandas
    '''
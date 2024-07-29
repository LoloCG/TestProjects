import os
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt

sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Pandas\Excel')
excel_ImpExp = __import__('module_excel_ImportExport_functs')

main_dir = os.path.dirname(os.path.abspath(__file__))

# df_raw = pd.read_csv(file_path, encoding='utf-16', delimiter='\t', skiprows=1)
# unique_period = df_raw['Period'].unique() # results = ['Summer' '1st semester' 'TODO:' '2nd Semester' 'Recu']

def main():

    #chosen_file = excel_ImpExp.select_excelFile_fromFolder(main_dir)
    chosen_file = '3º FarmNutr TDL_Log.csv'

    file_path = os.path.join(main_dir, chosen_file) 
    
    df_raw = pd.read_csv(file_path, encoding='utf-16', delimiter='\t', skiprows=1)
    
    df_clean = basic_raw_pretreatment(df_raw)

    hours_subject = total_hours_subjects(df_clean)

    plot_results_side_by_side(hours_subject)
    #plot_results_basic(hours_subject)


def basic_raw_pretreatment(df_raw):
    last_column = df_raw.columns[len(df_raw.columns)-1] # Obtains the name of the last column ("path")

    # Splits the last column into 3, adds them into df_raw  
    df_raw[['Period', 'Subject', 'Path3']] = df_raw[last_column].str.split('\\', n=2, expand=True)

    # Replaces commas with dots and convert to numeric the column of time spent
    df_raw['Time Spent (Hrs)'] = df_raw['Time Spent (Hrs)'].str.replace(',', '.').astype(float)
    
    df_clean = df_raw

    return df_clean
    
def total_hours_bothSemesters(dataframe):
    # Filtering for only '1st semester' and '2nd Semester'
    Only_Sem = df_clean[df_clean['Period'].isin(['1st semester', '2nd Semester'])]
        # the same can be obtained with:
        # Only_Sem = dataframe[(dataframe['Period'] == '1st semester') | (dataframe['Period'] == '2nd Semester')]   

    # Groups hours spent by column period
    grouped_sum = Only_Sem.groupby('Period')['Time Spent (Hrs)'].sum() 

    print(grouped_sum)

def total_hours_subjects(dataframe):
    # Filters for only '1st semester' and '2nd Semester'
    sem1_and_2 = dataframe[dataframe['Period'].isin(['1st semester', '2nd Semester'])]

    # Group by the 'Period' and 'Subject' columns and sum the 'Time Spent (Hrs)' column
    grouped_sum = sem1_and_2.groupby(['Period', 'Subject'])['Time Spent (Hrs)'].sum().reset_index()
    
    # Filter out rows where 'Time Spent (Hrs)' is less than 1
    grouped_sum = grouped_sum[grouped_sum['Time Spent (Hrs)'] >= 5]

    return(grouped_sum)


main()  


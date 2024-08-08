import os
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt

def main():
    chosen_file = '3º FarmNutr TDL_Log.csv'
    sys.path.append(r'C:\Users\Lolo\Desktop\Programming\GITRepo\PythonLearn-Resources\Data analysis\Pandas\Excel')

    excelCSV_raw = ExcelDataExtract()
    excelCSV_raw.csv_to_dataframe(chosen_file)
    
    #DEBUG: print(f"in main, df from CSV type: {type(excelCSV_raw.dataframe)}")

    df_clean = DataCleaner(excelCSV_raw.dataframe)
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

class DataFrameTransformer:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe
        print()

    def pivot_dataframe(self):
        df = self.dataframe
        # (index='indexCol', columns='columns', values='valueColumns')

        self.dataframe = df

    def filter_df_column_by_val(self,ColToFilter,FilterValues):
        print(f"Filtering dataframe for values {list(FilterValues)} located in column '{ColToFilter}'...")

        df = self.dataframe
        df = df[df[ColToFilter].isin(FilterValues)]
        self.dataframe = df
    
    def multiIndex_group(self, colsToGroup):
        '''
        From a dataframe of 3 columns, groups the numerical values by 
            two categorical value columns of a dataframe, returning an index-reset dataframe
        
        Parameters:
            df (dataframe), that is pre-processed. It can include other columns that 
                are not going to be grouped, as the function will only select those that will.
            
            colsToGroup (list), must include 3 column names as string which must be in the following order:
                numerical data, greater categorical data, lower categorical data.
        '''
        print(f"Grouping {colsToGroup[0]} by {colsToGroup[1]} and {colsToGroup[2]}...")

        df = self.dataframe
        df = df[colsToGroup]
        df = df.groupby([colsToGroup[1],colsToGroup[2]]).sum().reset_index()

        self.dataframe = df
    
class ExcelDataExtract:
    def __init__(self,chosen_file = None):
        print()
        self.main_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_folder_dir = None
        self.chosen_file = chosen_file
        self.dataframe = None

    def csv_to_dataframe(self, chosen_file, encoding=None, delimiter=None, skiprows=None):
        targetfile_path = os.path.join(self.main_dir, chosen_file)
        print(f"Extracting file {chosen_file}")
        df_raw = pd.read_csv(targetfile_path, encoding='utf-16', delimiter='\t', skiprows=1) # TODO: make dynamic selector of encoding, delimiter, skiprows...
        
        #DEBUG: print(f"Extracted df:\n{df_raw.head()}") 
        #DEBUG: print(f"returning type: {type(df_raw)}")

        self.dataframe = df_raw

    def show_folder_excel_files(self, folder_dir, file_type = None):
        '''
        Searches the folder given for any excel extension file, printing any that exist and returning a list of the file names.
        
        Parameters:
        folder_dir (str): The directory to search for Excel files.

        
        folder_excels (list): a list of strings of the excel files that are located in the folder direction.
        '''
        if not os.path.exists(folder_dir):
            print(f"Directory {folder_dir} does not exist.")
            return []
        if not os.path.isdir(folder_dir):
            print(f"{folder_dir} is not a directory.")
            return []
        
        folder_files = os.listdir(folder_dir)
        folder_excels = [file for file in folder_files if file.endswith(('.csv', '.xlsx', '.xls', '.xlsm'))]

        print("Files in the folder:")
        for index, file in enumerate(folder_excels):
            print(f"{index + 1}: {file}")

        return folder_excels

    def select_excelFile_fromFolder(self, file_type = None):
        while True:
            try:
                choice = int(input(f"Enter the number of the file you want to open (1-{len(input_excels)}): "))
                if 1 <= choice <= len(input_excels):
                    file = input_excels[choice - 1]
                    break
                else:
                    print(f"Please enter a number between 1 and {len(input_excels)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        print(f"chosen file: {file}")
        self.chosen_file = file

class DataCleaner:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def convert_dataframe_dates(self, removeDateCol=False):
        '''
        Converts a dataframe with unformatted dates into the datetime type of pandas.

        Parameters
            df (DataFrame), the raw dataframe without formatted datetime date variables.
            removeDateCol (bool), wether to keep (False) or delete (True) the old column of dates. Default false.
        '''
        print("Converting dataframe dates into datatime type...")
        #DEBUG: print("DataFrame columns before conversion:", list(self.dataframe.columns))
        
        if 'Start Date' not in self.dataframe.columns:
            raise KeyError("The DataFrame does not contain a 'Start Date' column.")
        
        df = self.dataframe

        df['date'] = pd.to_datetime(df['Start Date'])
        # Extract year, month, and day 
        df['year'] = df['date'].dt.year 
        df['month'] = df['date'].dt.month 
        df['day'] = df['date'].dt.day

        if removeDateCol:
            df.drop('Start Date', axis=1,inplace=True)

        self.dataframe = df

    def basic_raw_pretreatment(self):
        '''
        Does a basic precleaning of the dataset required for most typical functions required for analyzing academic study hours

        Parameters
            df_raw (DataFrame), the raw dataframe without pre-treatment

        Returns
            df_clean (DataFrame)
        '''
        print("Doing data pre-treatment...")
        last_column = 'Path'
        df_raw = self.dataframe

        # Splits the last column into 3, adds them into df_raw  
        df_raw[['Period', 'Subject', 'Path3']] = df_raw[last_column].str.split('\\', n=2, expand=True)

        df_raw['Time Spent (Hrs)'] = df_raw['Time Spent (Hrs)'].str.replace(',', '.').astype(float) # Replaces commas with dots and convert to numeric the column of time spent
        
        df_raw['Subject'] = df_raw['Subject'].str.strip().str.lower() # Normalize the subject names

        # print(f"Pre-cleaned data:\n{df_clean.head(3)}")
        
        self.dataframe = df_raw

    def show_missing_files(self):
        df_raw = self.dataframe
        if df_raw.isnull().any().any():
            empty_columns = df_raw.columns[df_raw.isnull().any()]

            if len(empty_columns) > 0:
                print(f"\nColumns that have empty values: ")
                for column in empty_columns:
                    empty_values = df_raw[column].isnull().sum()
                    # empty_values = df_raw[column[df_raw.isnull().sum()]]
                    print(f"- '{column}', with {empty_values}")

                    if empty_values == len(df_raw):
                        print(f"column '{column}' is completely empty ")
        else:
            print("No missing values in the dataset.")

class DataPlotter:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

        self.categorical_columns = None
        self.numerical_columns = None
        self.highest_hierarchy_column = None

        print()

    def identify_column_hierarchy(self):
        df = self.dataframe
        cat_cols = []
        Num_col = None
        num_uniq_val = 0
        first_hier_col = None

        for colname in df:
            coltype = str(df[colname].dtype)
            if coltype == 'object': 
                cat_cols.append(colname)

                if df[colname].value_counts().mean() > num_uniq_val:
                    
                    num_uniq_val = df[colname].value_counts().mean()
                    first_hier_col = colname

            elif coltype in ['float64','int64']:
                Num_col = colname

        #print(f"Category columns: {list(cat_cols)}")
        #print(f"Numerical columns: {Num_col}")
        print(f"Categorical columm with highest hierarchy: {first_hier_col}")
        #categ_in_highest_hierarch = list(df[first_hier_col].unique())
        #print(f"Categories: {categ_in_highest_hierarch[0]}, {categ_in_highest_hierarch[1]}")

        self.highest_hierarchy_column = first_hier_col        
        self.categorical_columns = cat_cols
        self.numerical_columns = Num_col

    def plot_hierarchical_categorical_bar_chart(self):
        """
        Plots a bar chart using a DataFrame with two categorical columns and one numerical column,
        where one categorical column represents a higher hierarchy.

        Parameters:
        df (pd.DataFrame): DataFrame containing the data to plot. It should contain two categorical columns 
                        (one representing a higher hierarchy) and one numerical column.
        """
        # This is to be replaced later by a list parameter in the function...
        catCol1 = self.highest_hierarchy_column 
        catCol2 = list(set(self.categorical_columns) - {catCol1})[0]
        numCol = self.numerical_columns

        df = self.dataframe


        periods = df[catCol1].unique()

        print(f"Plotting bar chart of {numCol} per {catCol2}, separated by {catCol1}...")

        x_values_dict = {period: [] for period in periods}    # Initialize lists to store x values for each period

        fig, ax = plt.subplots(figsize=(10, 6))

        n = 1
        for period in periods:
            filt_df = df[df[catCol1] == period]  

            for subject in filt_df[catCol2]:
                # DEBUG: print(f"{n} - period: {period}, Subject: {subject}") 
                x_values_dict[period].append(n)
                n += 1

            x_values = x_values_dict[period]
            y_values = df.loc[df[catCol1] == period, numCol]
            ax.bar(x_values, y_values, width=0.8, label=period, align='center')

        # Customizing the x-ticks to match the subjects
        all_subjects = list(df[catCol2])
        ax.set_xticks(range(1, n))
        ax.set_xticklabels(all_subjects, rotation=45)

        ax.legend(title=catCol1)
        ax.set_xlabel(catCol2)
        ax.set_ylabel(numCol)
        chartTitle = numCol + " per " + catCol2
        plt.legend(title=chartTitle)
        plt.xticks(rotation=45)
        plt.tight_layout() 
        plt.show()

main()

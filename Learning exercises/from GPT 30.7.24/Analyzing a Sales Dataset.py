'''
    Project Description: Analyze sales data to find trends, seasonality, and make forecasts.

    Example Steps:

        X - Load the sales dataset using pandas.
        X - Perform data cleaning (e.g., handle missing values, correct data types).
        X - Analyze sales trends over different time periods (e.g., monthly, yearly).
        - Identify top-performing products. (Done by GPT at feedback)
        X - Visualize sales trends using matplotlib.

    Feedback from GPT:
        - Add error handling for file loading.
            - Ensure file is correctly loaded
            - Ensure all necessary columns are present and correctly typed.
        - Add more visualization types and improve plot aesthetics.
'''
import os
import pandas as pd
#import numpy as np
#import sys
import matplotlib.pyplot as plt

main_dir = os.path.dirname(os.path.abspath(__file__))

def main():
    file_path = os.path.join(main_dir,'input_data', 'Sales_Dataset.csv')

    df_raw = pd.read_csv(file_path) # encoding='utf-16', delimiter=','
    
    # ======================= (CODE MADE BY GPT) =======================
    # Check for missing values
    print(f"total missing values in dataset: \n{df_raw.isnull().sum()}\n")

    # Ensure correct data types
    print(f"dataset types: \n{df_raw.dtypes}\n")
    # ==================================================================

    df = convert_dataframe_dates(df_raw, True)
    
    # ======================= (CODE MADE BY GPT) =======================
    # Identify top-performing products
    top_products = df.groupby('product').sum().sort_values(by='sales', ascending=False).reset_index()
    print(f"\nTop products:\n{top_products}\n")
    # ==================================================================

    colsToGroup = ['sales', 'year', 'product']
    indx_multiGroup_sum = multiGroup_sum(df, colsToGroup)

    pivot_df = indx_multiGroup_sum.pivot(index=colsToGroup[1], columns=colsToGroup[2], values=colsToGroup[0])
    
    print(f"\npivoted df head:\n{pivot_df.head(5)}")

    plot_pivotDf(pivot_df)

    # ======================= (CODE MADE BY GPT) =======================
    # Plot monthly sales trends (GPT)
    monthly_sales = df.groupby(['year', 'month', 'product']).sum().reset_index()
    monthly_sales.pivot(index=['year', 'month'], columns='product', values='sales').plot(kind='line', figsize=(10, 6))
    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.show()
    # ==================================================================


def plot_pivotDf(df):
    '''
    Generates a bar chart from a dataframe. 
    '''
    df.plot(kind='bar', figsize=(10, 6))

    plt.title('Sales of Products Over Years', loc='center')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.legend(title='Product',loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=5, fancybox=True, shadow=True) # , , 
    plt.grid(axis='y')
    plt.tight_layout() 
    plt.show()

def multiGroup_sum(df, colsToGroup):
    '''
    From a dataframe of 3 columns, groups the numerical values by 
        two categorical value columns of a dataframe, returning an index-reset dataframe
    
    Parameters:
        df (dataframe), that is pre-processed. It can include other columns that 
            are not going to be grouped, as the function will only select those that will.
        
        colsToGroup (list), must include 3 column names as string which must be in the following order:
            numerical data, greater categorical data, lower categorical data.
    '''
    df_group = df[[colsToGroup[0], colsToGroup[1], colsToGroup[2]]]

    print(f"Grouping {colsToGroup[0]} by {colsToGroup[1]} and {colsToGroup[2]}")
    
    multiGroup_sum = df_group.groupby([colsToGroup[1],colsToGroup[2]]).sum()

    indx_multiGroup_sum = multiGroup_sum.reset_index()

    return indx_multiGroup_sum

def group_numCol_by_catCol(df, num_var, cat_var=None): 
    '''
    Used to group numeric variable column by a categorical one.

    Parameters:
        df (DataFrame), The one that contains all the pre-cleaned data. Does not require it to contain the only two columns, and can be given entirely
        num_var (str), the name of the column with the numerical data
        cat_var (str), the name of the column with the categorical data
        
    Returns:
        Grouped (DataFrameGroupBy type object), that consists on two columns of all numerical grouped by the categoricals
    '''
    df_group = df[[cat_var, num_var]] 
    print(f"grouping {num_var} by {cat_var}")
    grouped = df_group.groupby(cat_var)

    return grouped

def convert_dataframe_dates(df, removeDateCol=False):
    '''
    Converts a dataframe with unformatted dates into the datetime type of pandas.

    Parameters
    df (DataFrame), the raw dataframe without formatted datetime date variables.
    removeDateCol (bool), wether to keep (False) or delete (True) the old column of dates. Default false.
    '''
    print("Converting the column 'date' into datetime type")

    df['date'] = pd.to_datetime(df['date'])
    # Extract year, month, and day 
    df['year'] = df['date'].dt.year 
    df['month'] = df['date'].dt.month 
    df['day'] = df['date'].dt.day

    if removeDateCol:
        df.drop('date', axis=1,inplace=True)

    return df

main()

def top_performing():
    print("...")
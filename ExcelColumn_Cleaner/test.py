import pandas as pd
import numpy as np

def main():
    # Example dictionary of DataFrames
    df_dict = {
        'sheet1': pd.DataFrame({'X': [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5],
                                'Y': [0, 0, 1, 8, 27, 20, 15, 12, 9, 6, 3]}),
        'sheet2': pd.DataFrame({'X': [0, 1, 2, 3, 4, 5],
                                'Y': [0, 0, 0.5, 5, 10, 10]}),
        # Add more DataFrames as needed
    }

    # Loop through each sheet and DataFrame in the dictionary
    for sheet, df in df_dict.items():
        y_start = obtain_threshold_value(df)
        if y_start is not None:
            print(f"For {sheet}, the curve starts to increase significantly at Y = {y_start}")
        else:
            print(f"For {sheet}, no significant increase found.")

def obtain_threshold_value(df):
    """
    Function to identify the starting point of the curve increase.
    Assumes that the DataFrame 'df' has columns 'X' and 'Y' for the respective values.
    """
    x = df['X'].values
    y = df['Y'].values
    
    # Calculate the rate of change (derivative)
    dy_dx = np.diff(y) / np.diff(x)
    
    # Identify the point where the derivative first exceeds a small threshold
    threshold = 0.1  # You can adjust this threshold based on your data
    try:
        start_index = np.where(dy_dx > threshold)[0][0] + 1  # +1 to get the index in the original array
    except IndexError:
        # Handle the case where no point exceeds the threshold
        start_index = None
    
    if start_index is not None:
        x_start = x[start_index]
        y_start = y[start_index]
        return y_start
    else:
        return None

main()

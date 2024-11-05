# from 01_excercise c) Create a function that takes in a DataFrame as input parameter and plots a barplot with the columns that have missing values. 
# Put this function into a file called data_utils.py. When you come across more useful functions, you can store them in your data_utils module.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.cm as cm
import numpy as np

def plot_missing_values(df):
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]

    if not missing_values.empty:
        colors = plt.cm.tab20(np.arange(len(missing_values)) / len(missing_values))
        missing_values.plot(kind="bar", color=colors)
        plt.title("Missing Values")
        plt.xlabel("Column")
        plt.ylabel("Number of missing values")
        plt.xticks(rotation=45)

        plt.show()
    else:
        print("No missing Values in the DataFrame")

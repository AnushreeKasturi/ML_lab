import pandas as pd
import numpy as np


def load_data(filename):
    return pd.read_excel(filename, sheet_name="thyroid0387_UCI")


def normalize(df):

    numeric = df.select_dtypes(include=np.number).columns

    normalized_df = df.copy()

    for col in numeric:

        minimum = df[col].min()
        maximum = df[col].max()

        normalized_df[col] = (df[col] - minimum) / (maximum - minimum)

    return normalized_df


def main():

    filename = "Lab Session Data.xlsx"

    df = load_data(filename)

    normalized_df = normalize(df)

    print("Original Data (First 5 Rows)\n")
    print(df.head())

    print("\nNormalized Data (First 5 Rows)\n")
    print(normalized_df.head())


main()
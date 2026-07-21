import pandas as pd
import numpy as np


def load_data(filename):
    return pd.read_excel(filename, sheet_name="thyroid0387_UCI")


def has_outliers(column):

    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    return ((column < lower) | (column > upper)).any()


def impute_data(df):

    for col in df.columns:

        if df[col].dtype == "object":

            mode = df[col].mode()[0]
            df[col].fillna(mode, inplace=True)

        else:

            if has_outliers(df[col]):

                median = df[col].median()
                df[col].fillna(median, inplace=True)

            else:

                mean = df[col].mean()
                df[col].fillna(mean, inplace=True)

    return df


def main():

    filename = "Lab Session Data.xlsx"

    df = load_data(filename)

    print("Missing Values Before Imputation\n")
    print(df.isnull().sum())

    df = impute_data(df)

    print("\nMissing Values After Imputation\n")
    print(df.isnull().sum())


main()
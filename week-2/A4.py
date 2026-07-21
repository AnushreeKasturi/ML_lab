import pandas as pd
import numpy as np


def load_data(filename):
    return pd.read_excel(filename, sheet_name="thyroid0387_UCI")


def attribute_info(df):
    info = []

    for col in df.columns:
        dtype = df[col].dtype

        if dtype == 'object':
            datatype = "Categorical"
            encoding = "One-Hot Encoding (Nominal) / Label Encoding (Ordinal)"
        else:
            datatype = "Numeric"
            encoding = "Not Required"

        info.append((col, datatype, encoding))

    return info


def numeric_range(df):
    numeric = df.select_dtypes(include=np.number)

    ranges = {}

    for col in numeric.columns:
        ranges[col] = (numeric[col].min(), numeric[col].max())

    return ranges


def missing_values(df):
    return df.isnull().sum()


def outliers(df):
    numeric = df.select_dtypes(include=np.number)

    result = {}

    for col in numeric.columns:
        Q1 = numeric[col].quantile(0.25)
        Q3 = numeric[col].quantile(0.75)

        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        count = ((numeric[col] < lower) | (numeric[col] > upper)).sum()

        result[col] = count

    return result


def statistics(df):
    numeric = df.select_dtypes(include=np.number)

    stats = {}

    for col in numeric.columns:
        stats[col] = (numeric[col].mean(), numeric[col].std())

    return stats


def main():

    filename = "Lab Session Data .xlsx"

    df = load_data(filename)

    print("========== ATTRIBUTE INFORMATION ==========\n")

    for col, datatype, encoding in attribute_info(df):
        print(f"{col}")
        print(f"Datatype : {datatype}")
        print(f"Encoding : {encoding}\n")

    print("========== NUMERIC RANGE ==========\n")

    for col, values in numeric_range(df).items():
        print(f"{col}: Min = {values[0]}, Max = {values[1]}")

    print("\n========== MISSING VALUES ==========\n")
    print(missing_values(df))

    print("\n========== OUTLIERS ==========\n")

    for col, count in outliers(df).items():
        print(f"{col}: {count}")

    print("\n========== MEAN & STANDARD DEVIATION ==========\n")

    for col, values in statistics(df).items():
        print(f"{col}")
        print(f"Mean = {values[0]}")
        print(f"Standard Deviation = {values[1]}\n")


main()
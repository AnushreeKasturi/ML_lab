import pandas as pd
import numpy as np


def load_data():
    df = pd.read_excel("Lab Session Data (2).xlsx",
                       sheet_name="marketing_campaign")
    return df


def mean(data):

    total = 0

    for value in data:
        total = total + value

    return total / len(data)


def variance(data):

    avg = mean(data)

    total = 0

    for value in data:
        total = total + (value - avg) ** 2

    return total / len(data)


def std(data):

    return variance(data) ** 0.5


def my_statistics(df):

    data = df.select_dtypes(include=["number"])

    result = {}

    for col in data.columns:

        values = data[col].dropna().tolist()

        result[col] = [mean(values), std(values)]

    return result


def numpy_statistics(df):

    data = df.select_dtypes(include=["number"])

    result = {}

    for col in data.columns:

        values = data[col].dropna()

        result[col] = [np.mean(values), np.std(values)]

    return result


def main():

    df = load_data()

    my_result = my_statistics(df)

    np_result = numpy_statistics(df)

    print("Feature\t\tMy Mean\t\tNumpy Mean\t\tMy Std\t\tNumpy Std")
    print("-" * 90)

    for col in my_result:

        print(col,
              "\t",
              round(my_result[col][0], 2),
              "\t",
              round(np_result[col][0], 2),
              "\t",
              round(my_result[col][1], 2),
              "\t",
              round(np_result[col][1], 2))


main()
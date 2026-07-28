import pandas as pd
import numpy as np


def load_data():
    df = pd.read_excel("Lab Session Data (2).xlsx",
                       sheet_name="marketing_campaign")
    return df


def get_vectors(df):

    data = df.select_dtypes(include=["number"])

    a = data.iloc[0].tolist()
    b = data.iloc[1].tolist()

    return a, b


def dot_product(a, b):

    total = 0

    for i in range(len(a)):
        total = total + (a[i] * b[i])

    return total


def norm(a):

    total = 0

    for value in a:
        total = total + value ** 2

    return total ** 0.5


def main():

    df = load_data()

    a, b = get_vectors(df)

    my_dot = dot_product(a, b)
    np_dot = np.dot(a, b)

    my_norm_a = norm(a)
    np_norm_a = np.linalg.norm(a)

    my_norm_b = norm(b)
    np_norm_b = np.linalg.norm(b)

    print("My Dot Product")
    print(my_dot)
    print()

    print("Numpy Dot Product")
    print(np_dot)
    print()

    print("My Norm of Vector A")
    print(my_norm_a)
    print()

    print("Numpy Norm of Vector A")
    print(np_norm_a)
    print()

    print("My Norm of Vector B")
    print(my_norm_b)
    print()

    print("Numpy Norm of Vector B")
    print(np_norm_b)


main()
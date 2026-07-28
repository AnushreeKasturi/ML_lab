import pandas as pd
from scipy.spatial.distance import minkowski


def load_data():
    df = pd.read_excel("Lab Session Data (2).xlsx",
                       sheet_name="marketing_campaign")
    return df


def distance(a, b, p):

    total = 0

    for i in range(len(a)):
        total = total + abs(a[i] - b[i]) ** p

    return total ** (1 / p)


def get_vectors(df):

    data = df.select_dtypes(include=["number"])

    a = data.iloc[0].tolist()
    b = data.iloc[1].tolist()

    return a, b


def main():

    df = load_data()

    a, b = get_vectors(df)

    p = 3

    my_distance = distance(a, b, p)

    scipy_distance = minkowski(a, b, p)

    print("My Function")
    print(my_distance)
    print()

    print("Scipy Function")
    print(scipy_distance)
    print()

    if abs(my_distance - scipy_distance) < 0.000001:
        print("Both distances are equal")
    else:
        print("Both distances are different")


main()
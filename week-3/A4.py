import pandas as pd


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

    print("Manhattan Distance")
    print(distance(a, b, 1))
    print()

    print("Euclidean Distance")
    print(distance(a, b, 2))
    print()

    print("Minkowski Distance (p = 3)")
    print(distance(a, b, 3))


main()
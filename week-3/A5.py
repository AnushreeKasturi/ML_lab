import pandas as pd
import matplotlib.pyplot as plt


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

    p_values = []
    distances = []

    for p in range(1, 11):

        d = distance(a, b, p)

        p_values.append(p)
        distances.append(d)

        print("p =", p, " Distance =", d)

    plt.plot(p_values, distances, marker="o")
    plt.xlabel("p")
    plt.ylabel("Distance")
    plt.title("Minkowski Distance")
    plt.grid(True)
    plt.show()


main()
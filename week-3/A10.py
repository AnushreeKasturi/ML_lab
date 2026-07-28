import pandas as pd
import matplotlib.pyplot as plt


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


def histogram(data):

    plt.hist(data, bins=10)

    plt.title("Histogram of Income")
    plt.xlabel("Income")
    plt.ylabel("Frequency")
    plt.grid(True)

    plt.show()


def main():

    df = load_data()

    income = df["Income"].dropna().tolist()

    print("Mean")
    print(mean(income))
    print()

    print("Variance")
    print(variance(income))
    print()

    histogram(income)


main()
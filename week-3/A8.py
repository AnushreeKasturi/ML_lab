import pandas as pd


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


def statistics(df):

    data = df.select_dtypes(include=["number"])

    result = {}

    for col in data.columns:

        values = data[col].dropna().tolist()

        result[col] = [
            mean(values),
            variance(values),
            std(values)
        ]

    return result


def main():

    df = load_data()

    result = statistics(df)

    print("Feature\t\tMean\t\tVariance\t\tStandard Deviation")
    print("-" * 80)

    for col in result:

        print(col,
              "\t",
              round(result[col][0], 2),
              "\t",
              round(result[col][1], 2),
              "\t",
              round(result[col][2], 2))


main()
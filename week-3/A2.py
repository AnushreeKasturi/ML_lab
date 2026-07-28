import pandas as pd


def load_data():
    df = pd.read_excel("Lab Session Data (2).xlsx",
                       sheet_name="marketing_campaign")
    return df


def label(df, col):

    values = list(df[col].dropna().unique())

    mapping = {}

    for i in range(len(values)):
        mapping[values[i]] = i

    result = []

    for value in df[col]:
        result.append(mapping[value])

    return result, mapping


def onehot(df, col):

    values = list(df[col].dropna().unique())

    new_df = pd.DataFrame()

    for value in values:

        name = col + "_" + str(value)

        data = []

        for item in df[col]:

            if item == value:
                data.append(1)
            else:
                data.append(0)

        new_df[name] = data

    return new_df


def main():

    df = load_data()

    education, mapping = label(df, "Education")

    print("Label Encoding")
    print(mapping)
    print()

    marital = onehot(df, "Marital_Status")

    print("One Hot Encoding")
    print(marital.head())


main()
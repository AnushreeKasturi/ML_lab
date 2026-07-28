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

    data = []

    for value in df[col]:
        data.append(mapping[value])

    return data


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


def convert(df):

    new_df = df.copy()

    new_df["Education"] = label(new_df, "Education")

    marital = onehot(new_df, "Marital_Status")

    new_df = new_df.drop("Marital_Status", axis=1)

    new_df = pd.concat([new_df, marital], axis=1)

    return new_df


def main():

    df = load_data()

    print("Original Shape")
    print(df.shape)
    print()

    new_df = convert(df)

    print("New Shape")
    print(new_df.shape)
    print()

    print("First Five Rows")
    print(new_df.head())


main()
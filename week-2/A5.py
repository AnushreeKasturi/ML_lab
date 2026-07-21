import pandas as pd


def load_data(filename):
    return pd.read_excel(filename, sheet_name="thyroid0387_UCI")


def get_binary_data(df):
    binary_cols = []

    for col in df.columns:
        values = df[col].dropna().unique()

        if set(values).issubset({0, 1}):
            binary_cols.append(col)

    return df[binary_cols]


def calculate_similarity(v1, v2):
    f11 = f10 = f01 = f00 = 0

    for i in range(len(v1)):
        if v1[i] == 1 and v2[i] == 1:
            f11 += 1
        elif v1[i] == 1 and v2[i] == 0:
            f10 += 1
        elif v1[i] == 0 and v2[i] == 1:
            f01 += 1
        else:
            f00 += 1

    jc = f11 / (f11 + f10 + f01)

    smc = (f11 + f00) / (f11 + f10 + f01 + f00)

    return f11, f10, f01, f00, jc, smc


def main():

    filename = "Lab Session Data .xlsx"

    df = load_data(filename)

    binary_df = get_binary_data(df)

    vector1 = binary_df.iloc[0].values
    vector2 = binary_df.iloc[1].values

    f11, f10, f01, f00, jc, smc = calculate_similarity(vector1, vector2)

    print("First Binary Vector:")
    print(vector1)

    print("\nSecond Binary Vector:")
    print(vector2)

    print("\nf11 =", f11)
    print("f10 =", f10)
    print("f01 =", f01)
    print("f00 =", f00)

    print("\nJaccard Coefficient =", jc)

    print("Simple Matching Coefficient =", smc)

    if smc > jc:
        print("\nSMC is more appropriate because it considers both matching 1s and matching 0s.")
    else:
        print("\nJC is more appropriate because it considers only the presence of attributes (1s).")


main()
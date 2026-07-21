import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


def load_data(filename):
    return pd.read_excel(filename, sheet_name="thyroid0387_UCI")


def preprocess(df):

    for col in df.columns:

        if df[col].dtype == "object":
            df[col] = df[col].fillna(df[col].mode()[0])

            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])

        else:
            df[col] = df[col].fillna(df[col].mean())

    return df


def cosine_similarity(v1, v2):

    dot_product = np.dot(v1, v2)

    magnitude1 = np.sqrt(np.sum(v1 ** 2))

    magnitude2 = np.sqrt(np.sum(v2 ** 2))

    similarity = dot_product / (magnitude1 * magnitude2)

    return similarity


def main():

    filename = "Lab Session Data.xlsx"

    df = load_data(filename)

    df = preprocess(df)

    vector1 = df.iloc[0].values

    vector2 = df.iloc[1].values

    similarity = cosine_similarity(vector1, vector2)

    print("Vector 1:")
    print(vector1)

    print("\nVector 2:")
    print(vector2)

    print("\nCosine Similarity =", similarity)


main()
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
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


def jaccard(v1, v2):

    f11 = f10 = f01 = 0

    for i in range(len(v1)):
        a = 1 if v1[i] != 0 else 0
        b = 1 if v2[i] != 0 else 0

        if a == 1 and b == 1:
            f11 += 1
        elif a == 1 and b == 0:
            f10 += 1
        elif a == 0 and b == 1:
            f01 += 1

    if (f11 + f10 + f01) == 0:
        return 0

    return f11 / (f11 + f10 + f01)


def smc(v1, v2):

    f11 = f10 = f01 = f00 = 0

    for i in range(len(v1)):
        a = 1 if v1[i] != 0 else 0
        b = 1 if v2[i] != 0 else 0

        if a == 1 and b == 1:
            f11 += 1
        elif a == 1 and b == 0:
            f10 += 1
        elif a == 0 and b == 1:
            f01 += 1
        else:
            f00 += 1

    return (f11 + f00) / (f11 + f10 + f01 + f00)


def cosine(v1, v2):

    dot = np.dot(v1, v2)

    mag1 = np.linalg.norm(v1)

    mag2 = np.linalg.norm(v2)

    return dot / (mag1 * mag2)


def similarity_matrix(data, method):

    n = len(data)

    matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            matrix[i][j] = method(data[i], data[j])

    return matrix


def plot_heatmap(matrix, title):

    plt.figure(figsize=(8, 6))

    sns.heatmap(matrix, annot=True, cmap="YlGnBu")

    plt.title(title)

    plt.show()


def main():

    filename = "Lab Session Data.xlsx"

    df = load_data(filename)

    df = preprocess(df)

    data = df.iloc[:20].values

    jc_matrix = similarity_matrix(data, jaccard)

    smc_matrix = similarity_matrix(data, smc)

    cos_matrix = similarity_matrix(data, cosine)

    print("Jaccard Similarity Matrix")
    print(jc_matrix)

    print("\nSimple Matching Coefficient Matrix")
    print(smc_matrix)

    print("\nCosine Similarity Matrix")
    print(cos_matrix)

    plot_heatmap(jc_matrix, "Jaccard Coefficient Heatmap")

    plot_heatmap(smc_matrix, "Simple Matching Coefficient Heatmap")

    plot_heatmap(cos_matrix, "Cosine Similarity Heatmap")


main()
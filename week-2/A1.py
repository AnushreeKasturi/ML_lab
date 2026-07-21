import pandas as pd
import numpy as np


def load_data(filename, sheet_name="Purchase data"):
    return pd.read_excel(filename, sheet_name=sheet_name)


def get_matrices(df, feature_cols, target_col):
    X = df[feature_cols].values
    y = df[target_col].values
    return X, y


def get_dimension(X):
    return X.shape[1]


def get_num_vectors(X):
    return X.shape[0]


def get_rank(X):
    return np.linalg.matrix_rank(X)


def get_cost(X, y):
    return np.linalg.pinv(X) @ y


def print_results(X, y, dimension, vectors, rank, cost, feature_cols):
    print("Feature Matrix (X):")
    print(X)

    print("\nOutput Vector (y):")
    print(y)

    print("\nDimensionality of Vector Space:", dimension)
    print("Number of Vectors:", vectors)
    print("Rank of Feature Matrix:", rank)

    print("\nCost of Products")
    for name, value in zip(feature_cols, cost):
        print(f"{name} = {value}")


def main():
    filename = "Lab Session Data .xlsx"
    feature_cols = ["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]
    target_col = "Payment (Rs)"

    df = load_data(filename)
    X, y = get_matrices(df, feature_cols, target_col)

    dimension = get_dimension(X)
    vectors = get_num_vectors(X)
    rank = get_rank(X)
    cost = get_cost(X, y)

    print_results(X, y, dimension, vectors, rank, cost, feature_cols)


main()
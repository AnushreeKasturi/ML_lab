# Generated with assistance from ChatGPT (OpenAI)

import numpy as np
import pandas as pd


# ---------------------------------------------------------
# Load the marketing_campaign dataset
# ---------------------------------------------------------

file_path = r"C:\Users\anush\Downloads\sem5\ML_lab\week-2\Lab Session Data .xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="marketing_campaign"
)

print("Original dataset shape:")
print(df.shape)


# ---------------------------------------------------------
# Select numerical features
# ---------------------------------------------------------

numeric_columns = df.select_dtypes(
    include=[np.number]
).columns.tolist()

# Remove ID because it is an identifier,
# not a meaningful numerical feature for distance calculation.
if "ID" in numeric_columns:
    numeric_columns.remove("ID")

print("\nNumerical features used for distance calculation:")
print(numeric_columns)


# ---------------------------------------------------------
# Prepare feature matrix
# ---------------------------------------------------------

numeric_data = df[numeric_columns].copy()

# Replace missing numerical values with the
# corresponding column median.
numeric_data = numeric_data.fillna(
    numeric_data.median()
)

X = numeric_data.to_numpy(
    dtype=float
)

print("\nFeature matrix shape:")
print(X.shape)


# ---------------------------------------------------------
# Generalized Minkowski Distance
# ---------------------------------------------------------

def minkowski_distance(A, B, p):
    """
    Calculate generalized Minkowski distance
    between two vectors A and B.

    p = 1 -> Manhattan distance
    p = 2 -> Euclidean distance
    """

    A = np.asarray(A, dtype=float)
    B = np.asarray(B, dtype=float)

    if A.shape != B.shape:
        raise ValueError(
            "Both vectors must have the same dimensions."
        )

    if p <= 0:
        raise ValueError(
            "The order parameter p must be greater than zero."
        )

    distance = np.sum(
        np.abs(A - B) ** p
    ) ** (1 / p)

    return distance


# ---------------------------------------------------------
# Select two feature vectors
# ---------------------------------------------------------

A = X[0]
B = X[1]

print("\nVector A:")
print(A)

print("\nVector B:")
print(B)


# ---------------------------------------------------------
# Calculate Manhattan Distance
# ---------------------------------------------------------

manhattan_distance = minkowski_distance(
    A,
    B,
    1
)

print("\nManhattan Distance (p = 1):")
print(manhattan_distance)


# ---------------------------------------------------------
# Calculate Euclidean Distance
# ---------------------------------------------------------

euclidean_distance = minkowski_distance(
    A,
    B,
    2
)

print("\nEuclidean Distance (p = 2):")
print(euclidean_distance)


# ---------------------------------------------------------
# Test another Minkowski order
# ---------------------------------------------------------

p = 3

distance_p3 = minkowski_distance(
    A,
    B,
    p
)

print(f"\nMinkowski Distance (p = {p}):")
print(distance_p3)
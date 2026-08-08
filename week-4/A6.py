# Generated with assistance from ChatGPT (OpenAI)

import numpy as np
import pandas as pd
from scipy.spatial.distance import minkowski


# ---------------------------------------------------------
# Load the marketing_campaign dataset
# ---------------------------------------------------------

file_path = r"C:\Users\anush\Downloads\sem5\ML_lab\week-2\Lab Session Data .xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="marketing_campaign"
)

print("Dataset shape:")
print(df.shape)


# ---------------------------------------------------------
# Select numerical features
# ---------------------------------------------------------

numeric_columns = df.select_dtypes(
    include=[np.number]
).columns.tolist()

# ID is an identifier and is not used
if "ID" in numeric_columns:
    numeric_columns.remove("ID")

numeric_data = df[numeric_columns].copy()

# Handle missing numerical values
numeric_data = numeric_data.fillna(
    numeric_data.median()
)

X = numeric_data.to_numpy(
    dtype=float
)


# ---------------------------------------------------------
# Custom Minkowski Distance Function
# ---------------------------------------------------------

def minkowski_distance(A, B, p):
    """
    Calculate generalized Minkowski distance.
    """

    A = np.asarray(A, dtype=float)
    B = np.asarray(B, dtype=float)

    if A.shape != B.shape:
        raise ValueError(
            "Both vectors must have the same dimensions."
        )

    if p <= 0:
        raise ValueError(
            "p must be greater than zero."
        )

    return np.sum(
        np.abs(A - B) ** p
    ) ** (1 / p)


# ---------------------------------------------------------
# Select two customer feature vectors
# ---------------------------------------------------------

A = X[0]
B = X[1]


print("\nVector A:")
print(A)

print("\nVector B:")
print(B)


# ---------------------------------------------------------
# Compare Custom Function with SciPy
# ---------------------------------------------------------

print("\nComparison of Custom Function and SciPy:")
print("-----------------------------------------")

for p in range(1, 11):

    custom_distance = minkowski_distance(
        A,
        B,
        p
    )

    scipy_distance = minkowski(
        A,
        B,
        p=p
    )

    difference = abs(
        custom_distance - scipy_distance
    )

    print(
        f"p = {p} | "
        f"Custom = {custom_distance:.10f} | "
        f"SciPy = {scipy_distance:.10f} | "
        f"Difference = {difference:.10f}"
    )
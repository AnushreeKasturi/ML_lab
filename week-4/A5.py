# Generated with assistance from ChatGPT (OpenAI)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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

# ID is an identifier, so it is not used for distance
if "ID" in numeric_columns:
    numeric_columns.remove("ID")

print("\nNumerical features used:")
print(numeric_columns)


# ---------------------------------------------------------
# Handle missing numerical values
# ---------------------------------------------------------

numeric_data = df[numeric_columns].copy()

numeric_data = numeric_data.fillna(
    numeric_data.median()
)

X = numeric_data.to_numpy(
    dtype=float
)


# ---------------------------------------------------------
# Generalized Minkowski Distance Function
# ---------------------------------------------------------

def minkowski_distance(A, B, p):
    """
    Calculate the generalized Minkowski distance
    between two vectors.
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

    distance = np.sum(
        np.abs(A - B) ** p
    ) ** (1 / p)

    return distance


# ---------------------------------------------------------
# Select two customer vectors
# ---------------------------------------------------------

A = X[0]
B = X[1]

print("\nVector A:")
print(A)

print("\nVector B:")
print(B)


# ---------------------------------------------------------
# Calculate Minkowski distances for p = 1 to 10
# ---------------------------------------------------------

p_values = range(1, 11)
distances = []

print("\nMinkowski Distance Values:")
print("--------------------------")

for p in p_values:

    distance = minkowski_distance(
        A,
        B,
        p
    )

    distances.append(distance)

    print(
        f"p = {p}: distance = {distance:.6f}"
    )


# ---------------------------------------------------------
# Plot Minkowski Distance vs p
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    list(p_values),
    distances,
    marker="o"
)

plt.xlabel("Minkowski Order (p)")
plt.ylabel("Distance")
plt.title("Minkowski Distance for Different Values of p")

plt.xticks(
    list(p_values)
)

plt.grid(True)

plt.tight_layout()

plt.show()
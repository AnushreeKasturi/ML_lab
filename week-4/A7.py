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

print("Dataset shape:")
print(df.shape)


# ---------------------------------------------------------
# Select numerical features
# ---------------------------------------------------------

numeric_columns = df.select_dtypes(
    include=[np.number]
).columns.tolist()

# ID is an identifier, so it is not used
if "ID" in numeric_columns:
    numeric_columns.remove("ID")

print("\nNumerical features used:")
print(numeric_columns)


# ---------------------------------------------------------
# Handle missing values
# ---------------------------------------------------------

numeric_data = df[numeric_columns].copy()

numeric_data = numeric_data.fillna(
    numeric_data.median()
)


# ---------------------------------------------------------
# Create feature matrix
# ---------------------------------------------------------

X = numeric_data.to_numpy(
    dtype=float
)

print("\nFeature matrix shape:")
print(X.shape)


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
# Custom Dot Product
# ---------------------------------------------------------

def vector_dot_product(A, B):
    """
    Calculate the dot product of two vectors manually.
    """

    if len(A) != len(B):
        raise ValueError(
            "Vectors must have the same length."
        )

    result = 0

    for i in range(len(A)):
        result += A[i] * B[i]

    return result


# ---------------------------------------------------------
# Custom Euclidean Norm
# ---------------------------------------------------------

def euclidean_norm(A):
    """
    Calculate the Euclidean norm of a vector manually.
    """

    squared_sum = 0

    for value in A:
        squared_sum += value ** 2

    return np.sqrt(squared_sum)


# ---------------------------------------------------------
# Calculate Dot Product
# ---------------------------------------------------------

custom_dot = vector_dot_product(
    A,
    B
)

numpy_dot = np.dot(
    A,
    B
)


# ---------------------------------------------------------
# Calculate Euclidean Norm
# ---------------------------------------------------------

custom_norm = euclidean_norm(
    A
)

numpy_norm = np.linalg.norm(
    A
)


# ---------------------------------------------------------
# Display Results
# ---------------------------------------------------------

print("\n========== VECTOR OPERATIONS ==========")

print("\nCustom Dot Product:")
print(custom_dot)

print("\nNumPy Dot Product:")
print(numpy_dot)

print("\nDifference in Dot Product:")
print(abs(custom_dot - numpy_dot))


print("\nCustom Euclidean Norm:")
print(custom_norm)

print("\nNumPy Euclidean Norm:")
print(numpy_norm)

print("\nDifference in Euclidean Norm:")
print(abs(custom_norm - numpy_norm))
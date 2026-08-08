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

# ID is an identifier and is not used
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
# Custom Mean Function
# ---------------------------------------------------------

def calculate_mean(values):

    total = 0

    for value in values:
        total += value

    return total / len(values)


# ---------------------------------------------------------
# Custom Variance Function
# ---------------------------------------------------------

def calculate_variance(values):

    mean = calculate_mean(values)

    squared_sum = 0

    for value in values:
        squared_sum += (value - mean) ** 2

    return squared_sum / len(values)


# ---------------------------------------------------------
# Custom Standard Deviation Function
# ---------------------------------------------------------

def calculate_standard_deviation(values):

    variance = calculate_variance(values)

    return np.sqrt(variance)


# ---------------------------------------------------------
# Compare Custom Functions with NumPy
# ---------------------------------------------------------

print("\n========== COMPARISON WITH NUMPY ==========")

for column in numeric_columns:

    values = numeric_data[column].to_numpy(
        dtype=float
    )

    # Custom calculations
    custom_mean = calculate_mean(values)

    custom_variance = calculate_variance(values)

    custom_std = calculate_standard_deviation(
        values
    )

    # NumPy calculations
    numpy_mean = np.mean(values)

    numpy_variance = np.var(values)

    numpy_std = np.std(values)

    # Differences
    mean_difference = abs(
        custom_mean - numpy_mean
    )

    variance_difference = abs(
        custom_variance - numpy_variance
    )

    std_difference = abs(
        custom_std - numpy_std
    )

    print(f"\nFeature: {column}")

    print(
        f"Custom Mean       : {custom_mean:.6f}"
    )

    print(
        f"NumPy Mean        : {numpy_mean:.6f}"
    )

    print(
        f"Mean Difference   : {mean_difference:.10f}"
    )

    print(
        f"Custom Variance   : {custom_variance:.6f}"
    )

    print(
        f"NumPy Variance    : {numpy_variance:.6f}"
    )

    print(
        f"Variance Difference: {variance_difference:.10f}"
    )

    print(
        f"Custom Std Dev    : {custom_std:.6f}"
    )

    print(
        f"NumPy Std Dev     : {numpy_std:.6f}"
    )

    print(
        f"Std Dev Difference: {std_difference:.10f}"
    )
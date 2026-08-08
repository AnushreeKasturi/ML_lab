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

# ID is an identifier and is not useful for statistical
# analysis of customer behavior
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
    """
    Calculate the arithmetic mean manually.
    """

    total = 0

    for value in values:
        total += value

    return total / len(values)


# ---------------------------------------------------------
# Custom Variance Function
# ---------------------------------------------------------

def calculate_variance(values):
    """
    Calculate population variance manually.
    """

    mean = calculate_mean(values)

    squared_sum = 0

    for value in values:
        squared_sum += (value - mean) ** 2

    return squared_sum / len(values)


# ---------------------------------------------------------
# Custom Standard Deviation Function
# ---------------------------------------------------------

def calculate_standard_deviation(values):
    """
    Calculate standard deviation manually.
    """

    variance = calculate_variance(values)

    return np.sqrt(variance)


# ---------------------------------------------------------
# Calculate Statistics for Each Numerical Feature
# ---------------------------------------------------------

results = []

for column in numeric_columns:

    values = numeric_data[column].to_numpy(
        dtype=float
    )

    mean = calculate_mean(values)

    variance = calculate_variance(values)

    standard_deviation = calculate_standard_deviation(
        values
    )

    results.append([
        column,
        mean,
        variance,
        standard_deviation
    ])


# ---------------------------------------------------------
# Display Results
# ---------------------------------------------------------

results_df = pd.DataFrame(
    results,
    columns=[
        "Feature",
        "Mean",
        "Variance",
        "Standard Deviation"
    ]
)

print("\n========== STATISTICAL ANALYSIS ==========")

print(
    results_df.to_string(
        index=False
    )
)
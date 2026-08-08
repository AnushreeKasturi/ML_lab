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

print("Dataset shape:")
print(df.shape)


# ---------------------------------------------------------
# Select Income feature
# ---------------------------------------------------------

income = df["Income"].copy()


# ---------------------------------------------------------
# Handle missing values
# ---------------------------------------------------------

income = income.fillna(
    income.median()
)


# ---------------------------------------------------------
# Convert to NumPy array
# ---------------------------------------------------------

income_values = income.to_numpy(
    dtype=float
)


# ---------------------------------------------------------
# Calculate Mean
# ---------------------------------------------------------

mean_income = np.mean(
    income_values
)


# ---------------------------------------------------------
# Calculate Variance
# ---------------------------------------------------------

variance_income = np.var(
    income_values
)


# ---------------------------------------------------------
# Display Statistics
# ---------------------------------------------------------

print("\n========== INCOME STATISTICS ==========")

print(
    f"Mean Income     : {mean_income:.4f}"
)

print(
    f"Income Variance : {variance_income:.4f}"
)

print(
    f"Income Std Dev  : {np.std(income_values):.4f}"
)


# ---------------------------------------------------------
# Histogram
# ---------------------------------------------------------

plt.figure(
    figsize=(8, 5)
)

plt.hist(
    income_values,
    bins=20,
    edgecolor="black"
)

plt.xlabel("Income")

plt.ylabel("Number of Customers")

plt.title(
    "Distribution of Customer Income"
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.show()
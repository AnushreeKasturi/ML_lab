# Generated with assistance from ChatGPT (OpenAI)

import pandas as pd
import numpy as np


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
# Label Encoding Function
# ---------------------------------------------------------

def label_encode(data):
    """
    Performs label encoding on a categorical feature.
    """

    categories = list(
        pd.unique(data.dropna())
    )

    mapping = {
        category: index
        for index, category in enumerate(categories)
    }

    encoded = data.map(mapping)

    return encoded, mapping


# ---------------------------------------------------------
# One-Hot Encoding Function
# ---------------------------------------------------------

def one_hot_encode(data):
    """
    Performs one-hot encoding on a categorical feature.
    """

    categories = list(
        pd.unique(data.dropna())
    )

    encoded = np.zeros(
        (len(data), len(categories)),
        dtype=int
    )

    category_index = {
        category: index
        for index, category in enumerate(categories)
    }

    for i, value in enumerate(data):

        if pd.notna(value) and value in category_index:

            encoded[
                i,
                category_index[value]
            ] = 1

    column_names = [
        f"{data.name}_{category}"
        for category in categories
    ]

    encoded_df = pd.DataFrame(
        encoded,
        columns=column_names,
        index=data.index
    )

    return encoded_df


# ---------------------------------------------------------
# Identify categorical columns
# ---------------------------------------------------------

categorical_columns = df.select_dtypes(
    include=["object", "category"]
).columns.tolist()

print("\nCategorical columns:")
print(categorical_columns)


# ---------------------------------------------------------
# Label Encoding
# ---------------------------------------------------------

label_encoded_df = df.copy()

for column in categorical_columns:

    encoded_values, mapping = label_encode(
        df[column]
    )

    label_encoded_df[column] = encoded_values


print("\nShape after Label Encoding:")
print(label_encoded_df.shape)


# ---------------------------------------------------------
# One-Hot Encoding
# ---------------------------------------------------------

one_hot_parts = []

for column in categorical_columns:

    encoded_column = one_hot_encode(
        df[column]
    )

    one_hot_parts.append(
        encoded_column
    )


# Keep all non-categorical features
non_categorical_df = df.drop(
    columns=categorical_columns
)


# Combine numerical and one-hot encoded features
one_hot_encoded_df = pd.concat(
    [non_categorical_df] + one_hot_parts,
    axis=1
)


print("\nShape after One-Hot Encoding:")
print(one_hot_encoded_df.shape)


# ---------------------------------------------------------
# Dimensionality Comparison
# ---------------------------------------------------------

original_rows, original_columns = df.shape

label_rows, label_columns = label_encoded_df.shape

onehot_rows, onehot_columns = one_hot_encoded_df.shape


print("\n========== DIMENSIONALITY COMPARISON ==========")

print(
    f"Original dataset: "
    f"{original_rows} rows x {original_columns} columns"
)

print(
    f"After Label Encoding: "
    f"{label_rows} rows x {label_columns} columns"
)

print(
    f"After One-Hot Encoding: "
    f"{onehot_rows} rows x {onehot_columns} columns"
)


print("\nChange in number of features:")

print(
    "Label Encoding:",
    label_columns - original_columns
)

print(
    "One-Hot Encoding:",
    onehot_columns - original_columns
)
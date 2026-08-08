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

print("Original Dataset Shape:")
print(df.shape)


# ---------------------------------------------------------
# A2: Label Encoding
# ---------------------------------------------------------

def label_encode(data):
    """
    Performs label encoding on a categorical Series.
    """

    # Preserve the original order of categories
    categories = list(
        pd.unique(
            data.dropna()
        )
    )

    mapping = {
        category: index
        for index, category in enumerate(categories)
    }

    encoded = data.map(mapping)

    return encoded, mapping


# ---------------------------------------------------------
# A2: One-Hot Encoding
# ---------------------------------------------------------

def one_hot_encode(data):
    """
    Performs one-hot encoding on a categorical Series.
    """

    # Preserve the original order of categories
    categories = list(
        pd.unique(
            data.dropna()
        )
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

print("\nCategorical Columns:")
print(categorical_columns)


# ---------------------------------------------------------
# Apply Label Encoding
# ---------------------------------------------------------

print("\n========== LABEL ENCODING ==========")

label_encoded_df = df.copy()

for column in categorical_columns:

    encoded_values, mapping = label_encode(
        df[column]
    )

    label_encoded_df[
        column
    ] = encoded_values

    print(f"\nColumn: {column}")
    print("Mapping:", mapping)


print("\nDataset after Label Encoding:")
print(label_encoded_df.head())

print(
    "\nShape after Label Encoding:",
    label_encoded_df.shape
)


# ---------------------------------------------------------
# Apply One-Hot Encoding
# ---------------------------------------------------------

print("\n========== ONE-HOT ENCODING ==========")

one_hot_parts = []

for column in categorical_columns:

    encoded_column = one_hot_encode(
        df[column]
    )

    one_hot_parts.append(
        encoded_column
    )

    print(
        f"\nOne-Hot Encoded Column: {column}"
    )

    print(
        encoded_column.head()
    )


# Keep non-categorical columns unchanged
numerical_df = df.drop(
    columns=categorical_columns
)


# Combine numerical and encoded columns
one_hot_encoded_df = pd.concat(
    [numerical_df] + one_hot_parts,
    axis=1
)


print(
    "\nDataset after One-Hot Encoding:"
)

print(
    one_hot_encoded_df.head()
)

print(
    "\nShape after One-Hot Encoding:",
    one_hot_encoded_df.shape
)
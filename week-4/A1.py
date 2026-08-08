import pandas as pd

file_path = r"C:\Users\anush\Downloads\sem5\ML_lab\week-2\Lab Session Data .xlsx"

excel_file = pd.ExcelFile(file_path)

print("Available sheets:")
for sheet in excel_file.sheet_names:
    print(sheet)
# Generated with assistance from ChatGPT (OpenAI)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.spatial.distance import minkowski
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Path to the Excel workbook
file_path = r"C:\Users\anush\Downloads\sem5\ML_lab\week-2\Lab Session Data .xlsx"

# Load the marketing_campaign sheet
df = pd.read_excel(
    file_path,
    sheet_name="marketing_campaign"
)

# Display basic information
print("Dataset shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst five rows:")
print(df.head())
# Generated with assistance from ChatGPT (OpenAI)

import pandas as pd

# ---------------------------------------------------------
# Load the marketing_campaign sheet
# ---------------------------------------------------------

file_path = r"C:\Users\anush\Downloads\sem5\ML_lab\week-2\Lab Session Data .xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="marketing_campaign"
)

print("Dataset shape:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())


# ---------------------------------------------------------
# A1: Feature Datatype Identification
# ---------------------------------------------------------

# Measurement-scale classification of the features
measurement_scale = {

    "ID": "Nominal",

    "Year_Birth": "Interval",

    "Education": "Ordinal",

    "Marital_Status": "Nominal",

    "Income": "Ratio",

    "Kidhome": "Ratio",

    "Teenhome": "Ratio",

    "Dt_Customer": "Interval",

    "Recency": "Ratio",

    "MntWines": "Ratio",

    "MntFruits": "Ratio",

    "MntMeatProducts": "Ratio",

    "MntFishProducts": "Ratio",

    "MntSweetProducts": "Ratio",

    "MntGoldProds": "Ratio",

    "NumDealsPurchases": "Ratio",

    "NumWebPurchases": "Ratio",

    "NumCatalogPurchases": "Ratio",

    "NumStorePurchases": "Ratio",

    "NumWebVisitsMonth": "Ratio",

    "AcceptedCmp3": "Nominal",

    "AcceptedCmp4": "Nominal",

    "AcceptedCmp5": "Nominal",

    "AcceptedCmp1": "Nominal",

    "AcceptedCmp2": "Nominal",

    "Complain": "Nominal",

    "Z_CostContact": "Ratio",

    "Z_Revenue": "Ratio",

    "Response": "Nominal"
}


# ---------------------------------------------------------
# Display feature information
# ---------------------------------------------------------

print("\nFeature Datatype and Measurement Scale")
print("--------------------------------------")

for feature in df.columns:

    datatype = df[feature].dtype

    scale = measurement_scale.get(
        feature,
        "Not Classified"
    )

    print(
        f"{feature:<25} "
        f"Datatype: {str(datatype):<12} "
        f"Scale: {scale}"
    )
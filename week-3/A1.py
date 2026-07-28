import pandas as pd


def load_data():
    df = pd.read_excel("Lab Session Data (2).xlsx",
                       sheet_name="marketing_campaign")
    return df


def identify_datatypes(df):

    datatype = {
        "ID": "Nominal",
        "Year_Birth": "Ratio",
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

    return datatype


def main():

    df = load_data()

    datatype = identify_datatypes(df)

    print("Feature\t\t\tDatatype")
    print("-" * 40)

    for feature in df.columns:
        print(f"{feature:20} {datatype[feature]}")


main()
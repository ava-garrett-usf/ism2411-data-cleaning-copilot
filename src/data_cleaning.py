#Install required libraries (pandas)
import pandas as pd

#Import the raw data csv file
def load_data(file_path):
    raw_data = pd.read_csv(file_path)
    return raw_data


# Data Cleaning Steps
#1 Standardize column names
#2 Strip leading and trailing whitespace from ProdName and CATEGORY
#3 Handle missing Price and qty using dropna
#4 Remove  rows with negative qty or price

#1 Standardize column names by removing leading/trailing whitespace, converting to lowercase, and replacing spaces with underscores
def clean_column_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df
#2 Strip leading and trailing whitespace from ProdName and CATEGORY
def strip_whitespace(df):
    df['prodname'] = df['prodname'].str.strip()
    df['category'] = df['category'].str.strip()
    return df
#3 Handle missing Price and qty using dropna for rows with NaN values in these columns
def handle_missing_values(df):
    df = df.dropna(subset=['price', 'qty'])
    return df
#4 Remove rows with negative qty or price using dropna
def remove_invalid_rows(df):
    df["price"] = pd.to_numeric(df["price"], errors='coerce')
    df["qty"] = pd.to_numeric(df["qty"], errors='coerce')
    df = df[(df['price'] >= 0) & (df['qty'] >= 0)]
    return df


#Required output pipeline code block
if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())


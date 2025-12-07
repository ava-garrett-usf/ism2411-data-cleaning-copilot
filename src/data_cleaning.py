#Install required libraries (pandas)
import pandas as pd

#Import the raw data csv file
raw_data = pd.read_csv('data/raw/sales_data_raw.csv')

#Show the first few rows of the raw data
print("Raw Data Preview:")
print(raw_data.head())
# Data Cleaning Steps
#1 Standardize column names
#2 Strip leading and trailing whitespace from product names and categories
#3 Handle missing prices and quantities using dropna
#4 Remove  rows with negative quantity or price

#1 Standardize column names by removing leading/trailing whitespace, converting to lowercase, and replacing spaces with underscores
def standardize_column_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
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


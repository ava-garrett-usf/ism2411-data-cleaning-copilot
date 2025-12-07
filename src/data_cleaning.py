#Install required libraries (pandas)
import pandas as pd

#Import the raw data csv file
raw_data = pd.read_csv('data/raw/sales_data_raw.csv')

#Show the first few rows of the raw data
print("Raw Data Preview:")
print(raw_data.head())



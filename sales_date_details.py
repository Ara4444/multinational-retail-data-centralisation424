
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
import json
import requests
import pandas as pd


## Instances for each of the classes
data_cleaner = DataCleaning()
data_extractor = DataExtractor(api_key='yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX')
db_connector = DatabaseConnector()

if __name__ == "__main__":
 ## Line 17-25 is dealing with the extraction, cleaning and uploading of the sales details data from a JSON file
 url = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'
 sales_date_df = data_extractor.extract_sales_date_details_json(url)
 #print(df)
 cleaned_df = data_cleaner.clean_date_details(df=sales_date_df)
 cleaned_sales_date_df = cleaned_df
 final_date_df = data_cleaner.clean_date_columns(cleaned_sales_date_df)
 #print(final_date_df)
 table_name = 'dim_date_times'
 db_connector.upload_to_db(final_date_df, table_name)
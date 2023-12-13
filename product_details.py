from data_extraction import DataExtractor
from database_utils import DatabaseConnector
from data_cleaning import DataCleaning
import pandas as pd


## Instances for each of the classes
data_extractor = DataExtractor(api_key='yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX')
db_connector = DatabaseConnector()
data_cleaner = DataCleaning()

if __name__ == "__main__":
 ## Line 14-20 is dealing with the extraction, cleaning and uploading for the product details data from a CSV file stored in an AWS S3 bucket.
 s3_address = 's3://data-handling-public/products.csv'
 df_products = DataExtractor.extract_from_s3(s3_address)
 ##print(df_products)
 df_products['weight'] = df_products['weight'].apply(DataCleaning.convert_to_kg)
 cleaned_df_products = data_cleaner.clean_products_data(df=df_products)
 print(cleaned_df_products)
 db_connector.upload_to_db(cleaned_df_products,table_name='dim_products')




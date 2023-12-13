

from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
import pandas as pd

## Instances for each of the classes
data_cleaner = DataCleaning()
data_extractor = DataExtractor(api_key='yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX')
db_connector = DatabaseConnector()

if __name__ == "__main__":
 ## Line 15-22 is dealing with the extraction, cleaning and uploading of the User details data from an AWS RDS.
 user_data_tables = db_connector.list_db_tables("https://data-handling-public.s3.eu-west-1.amazonaws.com")
 #print(user_data_tables)
 table_name = 'legacy_users'
 user_data_df = data_extractor.read_rds_table(db_connector, table_name)
 #print(user_data_df)
 cleaned_data = data_cleaner.clean_user_data(user_data_df)
 table_name = 'dim_users'
 db_connector.upload_to_db(cleaned_data, table_name)


 ## Line 26-31 is dealing with the extraction, cleaning and uploading of the card details data from an AWS S3 Bucket.
 pdf_data = data_extractor.retrieve_pdf_data("https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf")
 #print(pdf_data)
 cleaned_card_data = data_cleaner.clean_card_details_data(pdf_data)
 #print(cleaned_card_data)
 data_connector = DatabaseConnector(creds_file_path="local,db_creds.yaml")
 db_connector.upload_to_db(cleaned_card_data, table_name="dim_card_details")


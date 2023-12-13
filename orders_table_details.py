from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

## Instances for each of the classes
data_cleaner = DataCleaning()
data_extractor = DataExtractor(api_key='yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX')
db_connector = DatabaseConnector()


if __name__ == "__main__":
 ## Line 12-19 is dealing with the extraction, cleaning and uploading for the orders table details data from an AWS RDS.
 content_in_file = db_connector.list_db_tables("https://data-handling-public.s3.eu-west-1.amazonaws.com")
 table_name = "orders_table"
 orders_data = data_extractor.read_rds_table(db_connector, table_name)
 #print(orders_data)
 cleaned_orders_data = data_cleaner.clean_orders_table(df=orders_data)
 #print(cleaned_orders_data)
 table_name = 'orders_table'
 db_connector.upload_to_db(cleaned_orders_data, table_name)



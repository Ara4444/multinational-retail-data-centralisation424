from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
import requests
import time

## Instances for each of the classes
data_extractor = DataExtractor(api_key='yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX')
data_cleaner = DataCleaning()
data_connector = DatabaseConnector(creds_file_path="db_creds.yaml")

if __name__ == "__main__":
 ## Line 14-16 is dealing with retrieving and listing the number of stores within the business through the use of an API.
 number_of_stores_endpoint = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
 num_stores = data_extractor.list_number_of_stores(number_of_stores_endpoint)
 print(f"Number of stores to extract: {num_stores}")


 ## Line 20-34 is dealing with retrieving, cleaning and uploading each store to an SQL Database through the use of an API.
 retrieve_store_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}'
 store_numbers = list(range(0,452))
 for store_number in store_numbers: 
  formatted_endpoint = retrieve_store_endpoint.format(store_number=store_number)
  try:
   retrieve_store_data = data_extractor.retrieve_stores_data(formatted_endpoint)
   cleaned_store_data = data_cleaner.clean_store_data(store_data=retrieve_store_data)
   data_connector.upload_store_data_to_db(cleaned_store_data, table_name='dim_store_details')
  except requests.exceptions.HTTPError as e:
   if e.response.status_code == 429:
    print(f"Rate limit exceeded. Waiting for some time before making the next request.")
    time.sleep(5)  
    print(f"HTTP Error: {e}")
  except Exception as e:
   print(f"An unexpected error occurred: {e}")




import pandas as pd
from sqlalchemy import create_engine
from database_utils import DatabaseConnector
import tabula
import requests
import json
import boto3
from io import BytesIO, StringIO
import botocore

class DataExtractor():
 """
 This Class is designed to extract data from different data sources.
 """
 def __init__(self, api_key):
  """
  Initialize the DataExtractor instance with the provided API key.

  Parameters:
   - api_key (str): The API key used for authentication when making data extraction requests
  """
  self.headers = {'x-api-key': api_key}
    
 def read_rds_table(self,db_connector,table_name):
  """ 
  This function is to connect to an existing database and extract data from the requested table within the database.
  
  Parameters:
   - db_connecter(DatabaseConnector): An instance of the DatabaseConnector() Class
   - table_name(str): A string representation of a table name within a database   
   
  Returns:
   - pd.DataFrame: A Pandas DataFrame containing the extracted data from the specified table
  """
  db_connector = DatabaseConnector()
  engine = db_connector.init_db_engine() 
  query = f"SELECT * FROM {table_name}"
  df = pd.read_sql(query, engine)
  return df
 
 def retrieve_pdf_data(self, link: str):
  """ 
  This function used tabula to read and extract data from a pdf file and returns it as a Pandas DataFrame, if no tables are found it will return
  an empty DataFrame.

  Parameters:
   - link(str): A string representation of a PDF link

  Returns:
   - Pd.DataFrame: A Pandas DataFrame containing the extracted data from the PDF link 
  """
  pdf_path = link

  try:
   dfs = tabula.read_pdf(pdf_path,  pages="all", multiple_tables=True)
    
   if dfs:
    combined_data = pd.concat(dfs, ignore_index=True)
    return combined_data

   else: 
    print("No tables found in the PDF.")
    return pd.DataFrame()
  except Exception as e:
   print(f"Error extracting data from PDF: {e}")
    
  return pd.DataFrame()
   
 def _make_api_request(self, endpoint):
  """
  This function is to make a request to an API using the GET method.
  
  Parameters:
   - endpoint(str): The API endpoing to make the request to
  
  Returns:
   - requests.Response: The response object from the API request

  Raises:
   - requests.HTTPError: If the API request returns an error status code. 
  """
  response = requests.get(endpoint, headers=self.headers)
  response.raise_for_status()  
  return response
 
 def list_number_of_stores(self, number_of_stores_endpoint):
  """
  This function retrieves and lists the number of stores from the specified endpoint.
    
  Parameters:
   - number_of_stores_endpoint(str): A string representation of an API endpoint to retrieve the number of stores
    
  Returns:
   - dict: A dict containing the response in JSON format from the API
  """
  response = self._make_api_request(number_of_stores_endpoint)
  return response.json()

 def retrieve_stores_data(self, store_endpoint):
  """
  This function retrieves the store details of every store from the specified endpoint.
   
  Parameters:
   - store_endpoint(str)?: A string representation of an API endpoint to retrieve the store details data
   
  Returns:
   - Pd.DataFrame: A Pandas Dataframe of the store details data
    
  Raises:
   - requests.HTTPError: If the API returns a error status code
   - requests.Exeception: If the method returns an unexpected error
   - requests.RequestExeception: If the Request to the API returns an error 
  """
  response = self._make_api_request(store_endpoint)

  try:
    response.raise_for_status()
    store_data = response.json()
    if isinstance(store_data, list):

            store_df = pd.DataFrame(store_data)
    else:
            
     store_df = pd.DataFrame([store_data])
     return store_df
  except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
  except requests.exceptions.RequestException as err:
    print(f"Request Error: {err}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

 
 def extract_from_s3(self,s3_address):
  """
  This function extracts data from an S3 bucket.
   
  Parameters:
   - s3_address(str): A string representation of the S3 address in the format 's3://bucket_name/file_key'.
   
  Returns:
   - Pd.DataFrame: A Pandas DataFrame containing the data extracted from the S3 file
  Notes:
   - This method uses the 'boto3' library to interact with AWS S3.
   - The S3 address is parsed to extract the bucket name and file key.
   - The content of the S3 file is retrieved and decoded from UTF-8.
   - The decoded content is read into a Pandas DataFrame using StringIO.
  """
  s3_client = botocore.session.get_session().create_client('s3', config=botocore.config.Config(signature_version=botocore.UNSIGNED))
  bucket, key = s3_address.split('//')[1].split('/', 1)
  response = s3_client.get_object(Bucket=bucket, Key=key)
  csv_content = response['Body'].read().decode('utf-8')
  df = pd.read_csv(StringIO(csv_content))
  return df
 
 def extract_sales_date_details_json(self, url):
  sales_date_df = pd.read_json(url)
  return sales_date_df
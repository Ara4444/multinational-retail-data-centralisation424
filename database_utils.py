import yaml
from sqlalchemy import create_engine, inspect
from sqlalchemy.exc import SQLAlchemyError
import psycopg2

class DatabaseConnector():
 """ 
 A class to handle the connection to a database using SQLAlchemy.
 """
 def __init__(self, creds_file_path='db_creds.yaml'):
  """
  Initializes a DatabaseConnector instance.

  Parameters:
   - creds_file_path (str): The file path to the YAML file containing database credentials
  """
  self.creds= creds_file_path
  self.engine = self.create_engine()
  self.read_db_creds = self.read_db_creds()
  self.aws_engine = self.init_db_engine()
  
  


 def read_db_creds(self, file_path='db_creds.yaml'):
  """ 
  A function that reads the credentials within the YAML file.

  Parameters:
   - file_path(str): Path of the YAML file which contains the credentials
    
  Returns:
   - credentials(dict): Returns the database credentials in the form of a dictionary
  """ 
    # Read and Load the credentials needed from a YAML file
  with open(file_path, 'r') as file:
   creds = yaml.safe_load(file)
   return creds

 def init_db_engine(self, creds= "db_creds.yaml"):
  """
  This function initializes and returns a SQLAlchemy database engine for AWS connections.

  Parameters:
   - creds (str): The file path to the YAML file containing AWS database credentials

  Returns:
   - sqlalchemy.engine.base.Engine: The SQLAlchemy database engine for AWS connections
  """
  with open(creds, 'r') as file:
   creds = yaml.safe_load(file)
    # The creds needed to construct the database URL which hold the data needed for extraction
  aws_db_url = f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
    # Creating the engine instance needed to make the necessary connections
  aws_engine = create_engine(aws_db_url)
  return aws_engine
 
 def create_engine(self, db_file_path="local_db_creds.yaml"):
  """
  This function creates and returns a SQLAlchemy database engine on your local machine
  
  Parameters:
   - db_file_path(str): A string representation of the YAML file path containing the database credentials to your local machine

  Returns:
   - sqlalchemy.engine.base.Engine: The SQLAlchemy database engine
  """
    # Accessing local credentials within a YAML file
  with open(db_file_path, "r") as f:
   db_creds = yaml.safe_load(f)
    #  Contructing the local database URL needed for the uploading of the cleaned data
  db_url = f"postgresql://{db_creds['USER']}:{db_creds['PASSWORD']}@{db_creds['HOST']}:{db_creds['PORT']}/{db_creds['DATABASE']}"
    # Creating the engine instance needed to make the necessary connections
  engine = create_engine(db_url)
  return engine


 
 def list_db_tables(self, file):
  """
  This function is used to inspect and retrieve information of the tables.

  Returns: 
   - list: A list of tables
  """
    # Inspecting and Retreiving the table names from the database
  inspector = inspect(self.init_db_engine())
  tables = inspector.get_table_names()
  return tables
 

 def upload_to_db(self,df, table_name):
  """
  This function uploads a DataFrame to the specified table in the database. 

  Parameters:
   - df (pd.DataFrame): The Pandas DataFrame to be uploaded
   - table_name (str): The name of the table to which the data will be uploaded
  """
    # Connecting to the database
  connection = self.engine.connect()
    # Initiating a transaction for data upload
  transaction = connection.begin()
  try:
    # Uploading the DataFrame to a specified table and replacing existing tables
   df.to_sql(table_name, con=connection, if_exists='replace', index=False)
   print(f"Data uploaded to {table_name} successfully.")
    # Committing the upload if successful
   transaction.commit()
  except Exception as e:
    # Rolling back the transaction if an error occurs
    transaction.rollback()
    raise e
  finally:
    # Finally closing the database connection
    connection.close()


 def upload_store_data_to_db(self,df, table_name):
  """
  This function uploads a DataFrame to the specified table in the database, appending the data.

  Parameters:
   - df (pd.DataFrame): The Pandas DataFrame to be uploaded.
   - table_name (str): The name of the table to which the data will be appended.
  """
    # Connecting to the database
  connection = self.engine.connect()
    # Initiating a transaction for data upload
  transaction = connection.begin()
  try:
    # Uploadind the store DataFrame to a specified table and appending if there is an existing table  
   df.to_sql(table_name, con=connection, if_exists='append', index=False)
   print(f"Data uploaded to {table_name} successfully.")
    # Committing the upload if successful
   transaction.commit()
  except Exception as e:
    # Rolling back the transaction if an error occurs
    transaction.rollback()
    raise e
  finally:
    # Finally closing the database connection
    connection.close()

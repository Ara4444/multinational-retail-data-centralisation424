import pandas as pd
import re
import numpy as np

class DataCleaning():
 """
 This class is used to clean data extracted from different data sources.
 """
 def __init__(self) -> None:
  pass
 def clean_user_data(self,user_data_df):
  """
  This function is used to clean the user data by changing the datatype of specific columns and removing NULL or missing values.

  Parameters:
   - user_data_df (pd.DataFrame): Pandas DataFrame containing the user data

  Returns:
   - pd.DataFrame: Cleaned Pandas DataFrame
  """
    # Replacing NULL values with NaN and dropping rows with NaN values
  user_data_df.replace('NULL',np.nan,inplace=True)
  user_data_df.dropna(inplace=True)
    # Converting specified columns to datetime datatype and ignoring any errors
  user_data_df['date_of_birth'] = pd.to_datetime(user_data_df['date_of_birth'],errors='ignore')
    # Converting specified columns to datetime datatype and coercing errors
  user_data_df['join_date'] = pd.to_datetime(user_data_df['join_date'],errors='coerce')
    # Replacing 'GGB' with 'GB within the 'country_code' column
  user_data_df['country_code'] = user_data_df['country_code'].str.replace('GGB','GB')
    # Dropping any NULL values in the 'joint_date'column
  user_data_df = user_data_df.dropna(subset='join_date')
    #  Dropping duplicate rows based on the 'email_address' column
  user_data_df = user_data_df.drop_duplicates(subset=['email_address'])
    # Replacing any '.' or ' ' in the phone_number column
  need_to_replace = ['.', ' ']
  for i in need_to_replace:
   user_data_df['phone_number'] = user_data_df['phone_number'].str.replace(i,'')
    
    # Dropping the first column in the users_data
  user_data_df.drop(user_data_df.columns[0],axis=1, inplace=True)
  return user_data_df
 
 def clean_card_details_data(self, card_details_df: pd.DataFrame):
  """
  This function is used to clean the store data by dropping columns with unnecessary data,changing the datatype of specific columns, and removing any missing or NULL values.

  Parameters:
   - card_details_df(pd.DataFrame): Pandas DataFrame containing the card details data

  Returns:
   - pd.DataFrame: Cleaned Pandas DataFrame
  """
    # Converting the 'card_number' column to a string datatype
  card_details_df['card_number'] = card_details_df['card_number'].astype(str) 
    # Removing any non-numerical values 
  card_details_df['card_number'] = card_details_df['card_number'].str.replace('[^\d]', '')
    # Converting the 'card_number' column to a numeric datatype
  card_details_df['card_number'] = pd.to_numeric(card_details_df['card_number'], errors='coerce')
    # Dropping any NULL values in the 'card_number' column
  card_details_df = card_details_df.dropna(subset=['card_number'])
    # Converting 'card_number' column to a formatted string removing any decimal points
  card_details_df['card_number'] = card_details_df['card_number'].apply(lambda x: '{:.0f}'.format(float(x)))
  return card_details_df
 
 def convert_staffno_in__store_data_to_numeric(staff):
    # Extract only numeric characters from the staff number and return it as an integer
    numeric_part = re.sub(r'[^0-9.]', '', str(staff))
    return int(numeric_part)
 
 def clean_store_data(self, store_data: pd.DataFrame):
  """
  This function is used to perform cleaning on the store data such as dropping columns with unnecessary data, 
  change the datatype of specific columns to its suited datatype and also removing any missing or NULL value.

  Parameters:
   - store_data (pd.DataFrame): Pandas DataFrame containing store data

  Returns:
   - pd.DataFrame: Cleaned Pandas DataFrame
  """
    # Dropping the 'lat' column
  columns_to_drop = ['lat']
  cleaned_data = store_data.drop(columns_to_drop, axis=1)
    # Converting both 'longitude' and 'latitude' columns to a numeric datatype and coercing errors
  cleaned_data['longitude'] = pd.to_numeric(cleaned_data['longitude'], errors='coerce')
  cleaned_data['latitude'] = pd.to_numeric(cleaned_data['latitude'], errors='coerce')
    # Dropping any NULL values in the 'longitude' and 'latitude' columns
  cleaned_data = cleaned_data.dropna(subset=['longitude', 'latitude'])
    # Extracting numeric values from the 'staff_numbers' column
  cleaned_data['staff_numbers'] = cleaned_data['staff_numbers'].str.extract(pat='(\d+)', expand=False)
    # Replacing 'eeEurope' with 'Europe' and 'eeAmerica' with 'America' in the 'continent' column
  cleaned_data['continent'] = cleaned_data['continent'].str.replace('eeEurope','Europe')
  cleaned_data['continent'] = cleaned_data['continent'].str.replace('eeAmerica','America')
    # Dropping any NULL values in the cleaned_data DataFrame
  cleaned_data = cleaned_data.dropna()
  return cleaned_data
 
 def convert_to_kg(weight_str):
  """
  This function is used to convert values measured in millilitres(ml) or grams(g) into kilograms(kg) so that the 'weight' column 
   in the products data is all measured in the same metric.

  Parameters:
   - weight_str (string): A string representing the weight with a unit

  Returns:
   - float or None: The weight converted to kilograms Or returns None if the input is not a 
      valid weight string.
  """
  try:
    # Extracting digits and '.' from the input string and converting to a float
   weight = float(''.join(c for c in str(weight_str) if c.isdigit() or c in {'.'}))
  except ValueError:
   return None 
    # Checking the units in the input and converting to kg accordingly
  if 'kg' in str(weight_str):
   return weight
  elif 'g' in str(weight_str):
   return weight / 1000
  elif 'ml' in str(weight_str):
   return weight / 1000  
  else:
   return None  

 def clean_products_data(self, df):
  """
  This function is used to clean the product data such as removing any missing or NULL value and also drop any duplicate rows.

  Parameters:
   - df (pd.DataFrame): Pandas DataFrame containing product data

  Returns:
   - pd.DataFrame: Cleaned Pandas DataFrame
  """
    # Dropping any NULL values and duplicates in the specified DataFrame
  cleaned_df = df.dropna()  
  cleaned_df = cleaned_df.drop_duplicates()  
  return cleaned_df

 def clean_orders_table(self,df):
  """
  This function is used to clean the orders table data by dropping columns with unnecessary data.

  Parameters:
   - df (pd.DataFrame): Pandas DataFrame containing order_table data

  Returns:
   - pd.DataFrame: Cleaned Pandas DataFrame
  """
    # Dropping the 'first_name', 'last_name' and '1' columns
  columns_to_drop = ['first_name', 'last_name', '1']
  df = df.drop(columns=columns_to_drop)
  return df
 
 def clean_date_details(self, cleaned_df): 
  """
  This function is used to clean the sales date data by changing the datatype of specific columns and removing any missing or NULL value.

  Parameters:
   - df (pd.DataFrame): Pandas DataFrame containing sales date data

  Returns:
   - pd.DataFrame: Cleaned Pandas DataFrame
  """
    # Concatenating the 'year', 'month' and 'day' columns into one columns and converting it into datetime datatype
  cleaned_df['date'] = cleaned_df['year'].astype(str) + cleaned_df['month'].astype(str).str.zfill(2) + cleaned_df['day'].astype(str).str.zfill(2)
  cleaned_df['date'] = pd.to_datetime(cleaned_df['date'], errors='coerce')
    # Dropping any NULL values
  cleaned_df = cleaned_df.dropna()
  return cleaned_df
 

  
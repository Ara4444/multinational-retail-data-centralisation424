# Mutlinational Retail Data Centralisation(MRDC)
This project's main objective is to extract and clean the sales data for a multinational retail company located in different data sources
and make it accessible from one centralised location allowing for an efficient way to become a more data-driven company.

### File Structure
- **data_extraction.py**: A Class with multiple methods to extract data from different data sources 
- **data_cleaning.py A**: A Class with multiple methods to clean the data from different data sources  
- **database_utils.py**: A Class with methods that upload the cleaned data to a PostgreSQL Database database_utils.py
- **sql_queries** contains query files that deal with creating the schema of the database(ensuring correct datatypes,creating foreign keys and primary keys):
     - **orders_table_datatypes.sql**
     - **dim_users_datatypes.sql**
     - **dim_store_details_datatypes.sql**
     - **dim_products_datatypes.sql**
     - **dim_date_times_datatypes.sql**
     - **dim_card_details_datatypes.sql**
     - **creating_dim_pkeys.sql**
     - **creating_fkeys_order_table.sql**
 - **README.md**: A markdown file containing the documentation with essential information.
     
     

### Description
This project as stated above is to allow access to a company's sales data from one centralised location. These classes work with data that have been mainly
stored in various locations such as an API, CSV files, JSON files and Also in an AWS Database or an S3 bucket. Therefore certain methods would require credentials or API
keys for you to access the data (which ofcourse is not provided). Also this is mainly for uploading the data to a Database in Postgres.


### Usage/Installation
- Clone the Repo to your local machine in a terminal using the link below:
 ```
 https://github.com/Ara4444/multinational-retail-data-centralisation424.git
 ``` 
- The files you will find useful are mainly the Classes(listed above in Key-Features)
- The sql queries folder includes files that deal with the correction for the column datatypes for each table within the database.(Explanations of how and why are included
  within docstrings for each file. 

### Key-Notes
 - Ensure that you also provide the credentials needed for you to extract the information needed
 - Ensure to have your own credentials to upload a database on your local machine 
 - Make sure to run through the docstrings provided for each method with the Class to get a better undertstanding
 


### Additional-Notes
 - Also make any adjustments neccessary to make the code efficient in your cloned repo. A showcase of this would be also appreciated 

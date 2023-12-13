# Mutlinational Retail Data Centralisation(MRDC)
This project's main objective is to extract and clean the sales data for a multinational retail company located in different data sources
and make it accessible from one centralised location allowing for an efficient way to become a more data-driven company.

### Key-Features
- A Class with multiple methods to extract data from different data sources(code located in the file data_extraction.py)
- A Class with multiple methods to clean the data from different data sources(code located in the file data_cleaning.py)
- A Class with methods that upload the cleaned data to a PostgreSQL Database(code located in the file database_utils.py)
- The rest of the files are for the implemention and uses of the classes above for each of the unique data retrieved from the different data sources
  (list of these files:(user_and_card_details.py, store_details.py, product_details.py, orders_table_details.py and sales_date_details.py))

### Description
This project as stated above is to allow access to a company's sales data from one centralised location. These classes work with data that have been mainly
stored in various locations such as an API, CSV files, JSON files and Also in an AWS Database or an S3 bucket. Therefore certain methods would require credentionals or API
keys for you to access the data (which ofcourse is not provided). Also this is mainly for uploading the data to a Postgres Database.


### Usage/Installation
- Clone the Repo to your local machine
- The files you will find useful are mainly the Classes(listed above in Key-Features)


### Key-Notes
 - Ensure that you also provide the credentionals needed for you to extract the information needed
 - Ensure to have your own credentionals to upload a database on your local machine 
 - Make sure to run through the docstrings provided for each method with the Class to get a better undertstanding
 - The other Files are examples of how and what the methods are used for( In any case you do wish to get a better understanding of how they are used)


### Additional-Notes
 - Please if you also manange to compress and make the code more efficient. Access to that would be much appreciated and grateful

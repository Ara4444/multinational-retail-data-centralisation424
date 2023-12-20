# Mutlinational Retail Data Centralisation(MRDC)
This project's main objective is to extract and clean the sales data for a multinational retail company located in different data sources
and make it accessible from one centralised location allowing for an efficient way to become a more data-driven company.


### File Structure
- ```data_extraction.py```: A Class with multiple methods to extract data from different data sources 
- ```data_cleaning.py A```: A Class with multiple methods to clean the data from different data sources  
- ```database_utils.py```: A Class with methods that upload the cleaned data to a PostgreSQL Database database_utils.py
- **```sql_queries```**
 - contains query files that deal with creating the schema of the database(ensuring correct datatypes,creating foreign keys and primary keys):
     - ```orders_table_datatypes.sql```
     - ```dim_users_datatypes.sql```
     - ```dim_store_details_datatypes.sql```
     - ```dim_products_datatypes.sql```
     - ```dim_date_times_datatypes.sql```
     - ```dim_card_details_datatypes.sql```
     - ```creating_dim_pkeys.sql```
     - ```creating_fkeys_order_table.sql```
 - contains query files that deal with extracting business insights using the sales_date database(via JOINs, CTEs and Basic Aggregrations):
     - ```stores_in_each_country.sql```
     - ```locations_with_most_stores.sql```
     - ```month_largest_sales.sql```
     - ```online_vs_offline_sales.sql```
     - ```percentage_of_store_type.sql```
     - ```month_in_year_production.sql```
     - ```staff_headcount.sql```
     - ```germany_store_types.sql```
     - ```time_between_each_sale.sql```
 - ```README.md```: A markdown file containing the documentation with essential information.
 - ```.gitignore```: Contains files that is not for the public and git ignores.
 - ```LICENSE.txt```: A text file containing the details on MIT License used for this Project
     
     
### Description
This project as stated above is to allow access to a company's sales data from one centralised location. These classes work with data that have been mainly
stored in various locations such as an API, CSV files, JSON files and Also in an AWS Database or an S3 bucket. Therefore certain methods would require credentials or API
keys for you to access the data (which ofcourse is not provided). Also this is mainly for uploading the data to a Database in Postgres. Where then the job was to develop
the schema of the database and to ensure that the columns were converted to the correct datatypes. Once this was completed I would then use SQL to effectively extract 
valuable business insights to allow for the company to make decisions based on the data output of these queries.

### Usage/Installation
- Clone the Repo to your local machine in a terminal using the link below:
 ```
  git clone https://github.com/Ara4444/multinational-retail-data-centralisation424.git
  cd multinational-retail-data-centralisation424
 ``` 
- The files you will find useful are mainly the Classes(listed above in Key-Features)
- The sql queries folder includes files that deal with the correction for the column datatypes for each table within the database.(Explanations of how and why are included
  within docstrings for each file)
- The sql queries also included the querying to extract valuable business insights and the functions of each query is included within docstrings too.

### Key-Notes
 - Ensure that you also provide the credentials needed for you to extract the information needed
 - Ensure to have your own credentials to upload a database on your local machine 
 - Make sure to run through the docstrings provided for each method within the Class to get a better undertstanding of it's function(s)
 - Also note that many different libraries and python packages were used so please ensure you have the necessary packages installed ([required_packages.txt](required_packages.txt)).
 

### Additional-Notes
 - Also make any adjustments neccessary to make the code efficient in your cloned repo. A showcase of this would be also appreciated 


## License Info.
 - Licensed under the MIT License - Please direct yourself to the [LICENSE.txt](LICENSE.txt) file for the specifics.

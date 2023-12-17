-- Creating Primary Keys for dim tables which matches the same columns in the 'orders_table' table.

-- -- Each of the columns that make the Primary Key exist in the both the dim tables and 'orders_table' table.
 
ALTER TABLE dim_users
ADD PRIMARY KEY (user_uuid);

ALTER TABLE dim_store_details
ADD PRIMARY KEY (store_code);

ALTER TABLE dim_products
ADD PRIMARY KEY (product_code);

ALTER TABLE dim_date_times
ADD PRIMARY KEY (date_uuid);

ALTER TABLE dim_card_details
ADD PRIMARY KEY (card_number);

-- Creating Foreign keys to the orders_table columns to make the link between the primary keys created in the dim tables.

-- -- Note In some cases the dim tables have significantly less rows than the 'orders_table' therefore it would raise an error saying value does not exist.

-- -- -- The data in column 'product_code' in 'orders_table' that is not in column 'product_code' in 'dim_products' table.
SELECT orders_table.product_code
FROM orders_table
LEFT JOIN dim_products ON orders_table.product_code = dim_products.product_code
WHERE dim_products.product_code IS NULL;

-- -- -- Values in orders_table 'product_code' that are not present in dim_products 'product_code' and inserts those non-existing values into dim_products 'product_code'.
INSERT INTO dim_products (product_code)
SELECT DISTINCT orders_table.product_code
FROM orders_table
WHERE orders_table.product_code NOT IN (SELECT dim_products.product_code FROM dim_products);

-- -- -- The data in column 'card_number' in 'orders_table' that is not in column 'card_number' in dim_card_details table.
SELECT orders_table.card_number
FROM orders_table
LEFT JOIN dim_card_details ON orders_table.card_number = dim_card_details.card_number
WHERE dim_card_details.card_number IS NULL;

-- -- -- Values in orders_table 'card_number' that are not present in dim_card_details 'card_number' and inserts those non-existing values into dim_card_details 'card_number'.
INSERT INTO dim_card_details (card_number)
SELECT DISTINCT orders_table.card_number
FROM orders_table
WHERE orders_table.card_number NOT IN (SELECT dim_card_details.card_number FROM dim_card_details);

-- -- --  The data in column 'store_code' in orders_table that is not in column 'store_code' in dim_store_details table.
SELECT orders_table.store_code
FROM orders_table
LEFT JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
WHERE dim_store_details.store_code IS NULL;

-- -- -- Values in orders_table 'store_code' that are not present in dim_store_details 'store_code' and inserts those non-existing values into dim_store_details 'store_code'.
INSERT INTO dim_store_details (store_code)
SELECT DISTINCT orders_table.store_code
FROM orders_table
WHERE orders_table.store_code NOT IN (SELECT dim_store_details.store_code FROM dim_store_details);

-- -- -- The data in column 'user_uuid' in orders_table that is not in column 'user_uuid' in dim_users table.
SELECT orders_table.user_uuid
FROM orders_table
LEFT JOIN dim_users ON orders_table.user_uuid = dim_users.user_uuid
WHERE dim_users.user_uuid IS NULL;

-- -- -- Values in orders_table 'user_uuid' that are not present in dim_users 'user_uuid' and inserts those non-existing values into dim_users 'user_uuid'.
INSERT INTO dim_users (user_uuid)
SELECT DISTINCT orders_table.user_uuid
FROM orders_table
WHERE orders_table.user_uuid NOT IN (SELECT dim_users.user_uuid FROM dim_users);

-- -- -- Adding the foreign keys to 'order_table'

ALTER TABLE orders_table
ADD FOREIGN KEY (product_code) REFERENCES dim_products(product_code);

ALTER TABLE orders_table
ADD FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number);

ALTER TABLE orders_table
ADD FOREIGN KEY (store_code) REFERENCES dim_store_details(store_code);

ALTER TABLE orders_table
ADD FOREIGN KEY (user_uuid) REFERENCES dim_users(user_uuid);

ALTER TABLE orders_table
ADD FOREIGN KEY (date_uuid) REFERENCES dim_date_times(date_uuid);







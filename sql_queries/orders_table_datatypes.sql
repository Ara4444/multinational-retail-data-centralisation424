-- Casting columns of the 'orders_table' to the correct datatypes -- 

ALTER TABLE orders_table
ALTER COLUMN user_uuid TYPE UUID USING user_uuid::uuid;

ALTER TABLE orders_table
ALTER COLUMN date_uuid TYPE UUID USING date_uuid::uuid;

-- -- Checking max length of 'card_number' column
SELECT LENGTH(card_number) as len, card_number
FROM orders_table
GROUP BY card_number
ORDER BY len  
DESC; 
-- -- -- card_number max length: 19

ALTER TABLE orders_table
ALTER COLUMN card_number TYPE VARCHAR(19);

-- -- Checking max length of 'product_code' column
SELECT LENGTH(product_code) as len, product_code
FROM orders_table
GROUP BY product_code
ORDER BY len  
DESC; 
-- -- -- product_code max length: 11

ALTER TABLE orders_table
ALTER COLUMN product_code TYPE VARCHAR(11);

-- -- Checking max length of 'store_code' column
SELECT LENGTH(store_code) as len, store_code
FROM orders_table
GROUP BY store_code
ORDER BY len  
DESC; 
-- -- -- store_code max length: 12

ALTER TABLE orders_table
ALTER COLUMN store_code TYPE VARCHAR(12);

ALTER TABLE orders_table
ALTER COLUMN product_quantity TYPE SMALLINT;
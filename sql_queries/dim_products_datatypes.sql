-- Casting the 'dim_products' columns to the correct datatypes

-- -- Removing '£' sign from the 'product_price' column
UPDATE dim_products
SET product_price = REPLACE(product_price, '£', '')
WHERE product_price LIKE '£%';

-- -- Create a column 'weight_class' that defines the weight in 'weight' column either 'Light', 'Mid_Sized', 'Heavy' or 'Truck_required'
ALTER dim_products
ADD COLUMN weight_class VARCHAR(14);

UPDATE dim_products
SET weight_class = 
 CASE
   WHEN weight < 2 THEN 'Light'
   WHEN weight >= 2 AND weight < 40 THEN 'Mid_Sized'
   WHEN weight >= 40 AND weight < 140 THEN 'Heavy'
   WHEN weight => THEN 'Trucker_Required'
 END;

ALTER TABLE dim_products
ALTER COLUMN product_price TYPE FLOAT USING product_price::double_precision;

ALTER TABLE dim_products
ALTER COLUMN weight TYPE FLOAT USING weight::double_precision;

ALTER TABLE dim_products
ALTER COLUMN "EAN" TYPE VARCHAR(17);

ALTER TABLE dim_products
ALTER COLUMN product_code TYPE VARCHAR(11);

ALTER TABLE dim_products
ALTER COLUMN date_added TYPE USING DATE date_added::date;

-- -- Change column name 'removed' to 'still_available'
ALTER TABLE dim_products
RENAME COLUMN removed to still_available;

-- -- Set value 'Still_avaliable' = TRUE and 'Removed' = FALSE in the 'still_available' Column 
UPDATE dim_products
SET still_available = 
CASE
 WHEN still_avaliable = 'Still_avaliable' THEN TRUE
 WHEN still_available = 'Removed' THEN FALSE
 ELSE NULL
END;
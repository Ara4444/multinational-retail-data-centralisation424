-- The company is looking to increase its online sales.They want to know how many sales are happening online vs offline.
-- How many sales coming from online?

SELECT COUNT(product_quantity) AS number_of_sales, SUM(product_quantity) AS product_quantity_count,
CASE
 WHEN dim_store_details.store_code = 'WEB-1388012W' THEN 'Web'
 ELSE 'Offline'
END AS location
FROM orders_table
LEFT JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
GROUP BY location
ORDER BY product_quantity_count;

--- This query returns the no. of sales made and products sold online vs offline. 
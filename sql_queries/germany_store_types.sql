-- The sales team is looking to expand their territory in Germany. Determine which type of store is generating the most sales in Germany.
-- Which German store type is selling the most?

SELECT ROUND(SUM(dim_products.product_price * product_quantity)::numeric, 2) as total_sales,
       dim_store_details.store_type,
       dim_store_details.country_code
FROM orders_table
JOIN dim_products ON orders_table.product_code = dim_products.product_code
JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
WHERE dim_store_details.country_code = 'DE'
GROUP BY dim_store_details.store_type, dim_store_details.country_code
ORDER BY total_sales

--- This query returns the total amount of sales made in each of the different store types, listed from most to least.
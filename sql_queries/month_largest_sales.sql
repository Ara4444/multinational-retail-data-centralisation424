-- Which months produced the largest amount of sales?

SELECT dim_date_times.month, ROUND(SUM(dim_products.product_price*product_quantity)) as total_sales
FROM orders_table
JOIN dim_date_times ON dim_date_times.date_uuid = orders_table.date_uuid
JOIN dim_products ON dim_products.product_code = orders_table.product_code
GROUP BY dim_date_times.month
ORDER BY total_sales
DESC;

--- This query returns a table with the most to least sales generated for every month.


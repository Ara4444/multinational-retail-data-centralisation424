-- The company stakeholders want assurances that the company has been doing well recently.
-- Which month in each year produced the highest cost of sales?

SELECT ROUND(SUM(dim_products.product_price * product_quantity)::numeric, 2) as total_sales,
       dim_date_times.year,
       dim_date_times.month
FROM orders_table
JOIN dim_products ON orders_table.product_code = dim_products.product_code
JOIN dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid
GROUP BY dim_date_times.year, dim_date_times.month
ORDER BY total_sales
DESC;

--- This query returns the highest amount of sales made in a month in it's respected year. 


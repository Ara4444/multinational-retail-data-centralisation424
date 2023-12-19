-- The sales team wants to know which of the different store types is generated the most revenue so they know where to focus.
-- What percentage of sales come through each type of store?

SELECT COALESCE(dim_store_details.store_type, 'Web Portal') as store_type,
       ROUND(CAST(SUM(product_quantity * dim_products.product_price) as numeric), 2) AS total_sales,
       ROUND(CAST(SUM(product_quantity * dim_products.product_price) / (SELECT SUM(product_quantity * dim_products.product_price)
FROM orders_table
LEFT JOIN dim_products ON orders_table.product_code = dim_products.product_code) * 100 AS numeric), 2) AS "percentage_total(%)"
FROM orders_table
LEFT JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
LEFT JOIN dim_products ON orders_table.product_code = dim_products.product_code
GROUP BY store_type
ORDER BY total_sales DESC;

--- This query returns the total sales made in each of the store_types across all the stores represented in actual sales and also a percentage of the total_sales for each store type.
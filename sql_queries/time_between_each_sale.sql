-- Sales would like the get an accurate metric for how quickly the company is making sales.
-- How quickly is the company making sales?

-- -- Creation of CTE sale_date_time_difference so it takes in each row of the date_time column.
with sales_date_time_difference as (
SELECT year, date_time, LEAD(date_time) OVER (
ORDER BY date_time DESC) as next_sales_date_time
FROM dim_date_times )

SELECT year, AVG((date_time - next_sales_date_time)) as actual_time_taken
FROM sales_date_time_difference
GROUP BY year
ORDER BY actual_time_taken
DESC;

--- This query returns the average time taken between each sale made for each year.
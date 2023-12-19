-- The operations team would like to know the overall staff numbers in each location around the world.
-- What is the staff headcount?

SELECT SUM(staff_numbers) AS total_staff_numbers,country_code FROM dim_store_details
WHERE country_code IS NOT NULL
GROUP BY country_code
ORDER BY total_staff_numbers
DESC;

--- This query returns a clear headcount of the number of total staff in each country that we operate in.
-- The Operations team would like to know which countries we currently operate in and which country now has the most stores. 
-- How many stores does the business have and in which countries?

SELECT country_code,
CASE
 WHEN country_code = 'GB' THEN 'Great Britain'
 WHEN country_code = 'US' THEN 'United States'
 WHEN country_code = 'DE' THEN 'Germany'
END as country, COUNT(country_code) as total_no_stores
FROM dim_store_details
WHERE country_code IS NOT NULL
GROUP BY country_code
ORDER BY total_no_stores

--- This query returns the number of stores in every country. 
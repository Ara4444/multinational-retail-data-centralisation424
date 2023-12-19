-- The business stakeholders would like to know which locations currently have the most stores,They would like to close some stores before opening more in other locations.
-- Which Locations currently have the most stores?

SELECT locality , COUNT( locality ) as total_no_store FROM dim_store_details
GROUP BY locality
ORDER BY total_no_stores
DESC LIMIT 10;

--- This query returns a list of the Top 10 Locations with the most number of stores.



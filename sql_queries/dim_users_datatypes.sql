-- Casting the columns of the 'dim_users' table to the correct datatypes

ALTER TABLE dim_users
ALTER COLUMN first_name TYPE VARCHAR(255);

ALTER TABLE dim_users
ALTER COLUMN last_name TYPE VARCHAR(255);

ALTER TABLE dim_users
ALTER COLUMN date_of_birth TYPE DATE USING date_of_birth::date;

ALTER TABLE dim_users
ALTER COLUMN user_uuid TYPE UUID USING user_uuid::uuid;

ALTER TABLE dim_users
ALTER COLUMN join_date TYPE DATE USING date_of_birth::date;

-- -- Finding the max length of the 'country_code' column
SELECT LENGTH(country_code) as len , country_code FROM dim_users
GROUP BY country_code
ORDER BY len
DESC;
-- -- -- max length of country_code: 2

 ALTER TABLE dim_users
 ALTER COLUMN country_code TYPE VARCHAR(2);


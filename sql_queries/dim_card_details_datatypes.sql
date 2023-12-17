-- Casting the 'dim_card_details' columns to the correct datatypes

-- -- Finding the max length of the 'card_number' column
SELECT LENGTH(card_number) as len, card_number
FROM dim_card_details
GROUP BY card_number
ORDER BY len  
DESC;
-- -- -- max length of card_number: 19

ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE VARCHAR(19);

-- -- Finding the max length of the 'expiry_date' column
SELECT LENGTH(expiry_date) as len, expiry_date
FROM dim_card_details
GROUP BY expiry_date
ORDER BY len  
DESC;
-- -- -- max length of expiry_date: 5

ALTER TABLE dim_card_details
ALTER COLUMN expiry_date TYPE VARCHAR(5)

ALTER TABLE dim_card_details
ALTER COLUMN date_payment_confirmed TYPE DATE USING date_payment_confirmed::date;
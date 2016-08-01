-- MySQL Functions

SELECT concat(first_name, ' ', last_name) FROM clients;
SELECT CONCAT_WS(' ',first_name,last_name) AS bitches FROM clients;
SELECT LENGTH(last_name) AS last_name_length FROM  clients;
SELECT LOWER(last_name) AS lowercase_name FROM clients;

SELECT HOUR(joined_datetime) AS what_hour, joined_datetime FROM clients;
SELECT DAYNAME(joined_datetime) AS day_name, joined_datetime FROM clients;
SELECT MONTH(joined_datetime) AS month_number, joined_datetime FROM clients;
SELECT NOW() AS right_now;

-- w3schools.com/sql/func_date_format.asp
-- Date format
SELECT DATE_FORMAT(joined_datetime,'%W, %M %e, %Y') FROM clients;